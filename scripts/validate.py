#!/usr/bin/env python3
"""Validate the public Agent template index before publishing it."""

import json
import re
from pathlib import Path

INDEX = Path(__file__).resolve().parents[1] / "index.json"
SAFE_ID = re.compile(r"^[a-z][a-z0-9-]{1,63}$")
SAFE_ICON = re.compile(r"^[a-z0-9.]{2,60}$")
CAPABILITIES = {"ish_shell", "wk_browser", "calendar", "brightroom_photo"}


def check_text(value, maximum):
    assert isinstance(value, dict) and set(value) == {"zh", "en"}
    assert all(isinstance(value[lang], str) and 0 < len(value[lang].strip()) <= maximum for lang in ("zh", "en"))


def check_ids(values, maximum):
    assert isinstance(values, list) and len(values) <= maximum
    assert len(set(values)) == len(values)
    assert all(isinstance(item, str) and SAFE_ID.fullmatch(item) for item in values)


def main():
    raw = INDEX.read_bytes()
    assert len(raw) <= 256_000, "index.json exceeds 256 KB"
    index = json.loads(raw)
    assert index["schemaVersion"] == 1
    templates = index["templates"]
    assert isinstance(templates, list) and 0 < len(templates) <= 50
    seen = set()
    for item in templates:
        assert SAFE_ID.fullmatch(item["id"]) and item["id"] not in seen
        seen.add(item["id"])
        assert isinstance(item["version"], int) and 0 < item["version"] <= 10_000
        assert SAFE_ICON.fullmatch(item["icon"])
        for key, maximum in (("category", 50), ("title", 80), ("summary", 500), ("instruction", 8_000)):
            check_text(item[key], maximum)
        prompts = item["starterPrompts"]
        assert isinstance(prompts, list) and 1 <= len(prompts) <= 4
        for prompt in prompts:
            check_text(prompt, 300)
        check_ids(item["pluginIDs"], 8)
        check_ids(item["skillIDs"], 8)
        capabilities = item["capabilityIDs"]
        assert isinstance(capabilities, list) and len(capabilities) <= 12
        assert len(set(capabilities)) == len(capabilities) and set(capabilities) <= CAPABILITIES
        assert item["environment"] in {"local", "ssh"}
        assert type(item["requiresImageModel"]) is bool
    print(f"Validated {len(templates)} Agent templates")


if __name__ == "__main__":
    main()
