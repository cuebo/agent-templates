# Cuebo Agent Templates

This repository supplies the Agent template store in Cuebo. The app reads [`index.json`](index.json) from the `main` branch, validates it, and displays the templates as one list. It keeps the last valid catalog for offline use.

## Add a template

Add an object to `templates` in `index.json` and run `python3 scripts/validate.py`. Keep `id` stable and increase `version` when changing an existing template. Each template needs Chinese and English text for `category`, `title`, `summary`, `instruction`, and one to four `starterPrompts`. `icon` is an SF Symbol name.

`capabilityIDs` contains optional built-in capabilities. `pluginIDs` references IDs from [cuebo/plugins](https://github.com/cuebo/plugins), and `skillIDs` references IDs from [cuebo/skills](https://github.com/cuebo/skills). Cuebo shows missing dependencies and links to the corresponding store. Once installed, these IDs are enabled on the new Agent. The `pdf-report` template demonstrates both presets.

`systemCapabilities` optionally sets the per-Agent switches of the always-attached System Capability. Supported keys are `user_interaction`, `memory`, `scheduled_tasks`, `conversation_title`, `clipboard`, `location`, `plugins`, `conversations`, `agents`, `skills`, `models`, and `environments`; values must be booleans. An omitted key uses the new-Agent default: interaction, memory, scheduled tasks, conversation titles, and clipboard on; the remaining keys off. `skills` and `plugins` here grant **management** tools. Listing a Skill or plugin in `skillIDs` or `pluginIDs` only attaches that dependency and does not grant its management tools. Templates with no `systemCapabilities` remain valid.

`environment` is `local` or `ssh`. `requiresImageModel` tells the installer to require a model with image input. Templates never contain credentials, personal memory, or environment identifiers; users select their own model and SSH environment during installation. The selected model and environment are stored on the new Agent, while System Capability switches are copied from this template.

The store accepts at most 50 templates and a 256 KB index. Built-in capability IDs are limited to those supported by the app. Health and HomeKit are intentionally unavailable through catalog presets because they need separate permission choices.
