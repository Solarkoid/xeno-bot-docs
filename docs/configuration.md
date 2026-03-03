# Configuration

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
