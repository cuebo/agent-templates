# Cuebo Agent Templates

This repository supplies the Agent template store in Cuebo. The app reads [`index.json`](index.json) from the `main` branch, validates it, and displays the templates as one list. It keeps the last valid catalog for offline use.

## Add a template

Add an object to `templates` in `index.json` and run `python3 scripts/validate.py`. Keep `id` stable and increase `version` when changing an existing template. Each template needs Chinese and English text for `category`, `title`, `summary`, `instruction`, and one to four `starterPrompts`. `icon` is an SF Symbol name.

`capabilityIDs` contains optional built-in capabilities. `pluginIDs` references IDs from [cuebo/plugins](https://github.com/cuebo/plugins), and `skillIDs` references IDs from [cuebo/skills](https://github.com/cuebo/skills). Cuebo shows missing dependencies and links to the corresponding store. Once installed, these IDs are enabled on the new Agent. The `pdf-report` template demonstrates both presets.

`environment` is `local` or `ssh`. `requiresImageModel` tells the installer to require a model with image input. Templates never contain credentials, personal memory, or environment identifiers; users select their own model and SSH environment during installation.

The store accepts at most 50 templates and a 256 KB index. Built-in capability IDs are limited to those supported by the app. Health and HomeKit are intentionally unavailable through catalog presets because they need separate permission choices.
