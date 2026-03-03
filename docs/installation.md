# Installation


This project documents the `xeno-bot` Node.js project. To run or develop the bot itself, follow the upstream repository's Node/npm instructions.

Clone the bot repository (example):

```bash
git clone https://github.com/devvyyxyz/xeno-bot.git
cd xeno-bot
```

Install Node dependencies

```bash
node --version   # Node 18+ recommended
npm install
```

Environment

- Copy `.env.example` to `.env` and fill values (e.g. `TOKEN`, `CLIENT_ID`, optional `GUILD_ID`).
- `DATABASE_URL` — optional for Postgres/MySQL; otherwise dev uses local SQLite at `data/dev.sqlite`.

Run commands

```bash
# start in development (nodemon):
npm run dev

# production start (sharded by default):
npm start

# deploy slash commands (use with care):
npm run deploy:public
```

Docs site (this repository)

The documentation site is built with MkDocs. To edit/preview these docs, see this repo's README and run the MkDocs instructions in the docs root.

