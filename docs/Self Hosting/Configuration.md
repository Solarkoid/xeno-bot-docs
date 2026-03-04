---
title: Configuration
description: Xeno Bot is configured via a YAML file (`config.yml`) placed at the project root or specified with `--config`.
tags:
  - config
  - setup
  - instructions
  - self-hosting
keywords:
  - xeno
  - bot
  - config
  - documentation
author: Devvyyxyz
image: assets/images/faq-og.png
date: 2026-03-04
permalink: /configuration/
toc: true
icon: material/help-circle
aliases:
  - /config/
  - /configuration/
---

Xeno Bot is configured via a YAML file (`config.yml`) placed at the project root or specified with `--config`.

Example `config.yml`:

```yaml
bot:
  name: xeno
  token: "YOUR_TOKEN"
  prefix: "!"

logging:
  level: info

plugins:
  - name: echo
    enabled: true
```

Configuration options
- `bot.name`: display name
- `bot.token`: authentication token for platform
- `bot.prefix`: command prefix
- `plugins`: list of plugin configs
