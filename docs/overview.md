# Overview

Xeno Bot is a Discord bot scaffold built on discord.js v14 focused on scalability, modular commands, and extensible server-side configuration. This docs site documents the public repo at https://github.com/devvyyxyz/xeno-bot and provides onboarding, developer guidance, and architecture notes.

Key features

- Command-driven architecture (slash & message commands)
- Server-configurable behavior via `config/` and runtime `/.env`
- Database support via `knex` (SQLite for dev, Postgres/MySQL in production)
- Sharding support and production-ready deployment scripts
- Dashboard and web UI for server configuration (optional)
