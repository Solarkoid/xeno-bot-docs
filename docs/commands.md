# Commands

Xeno Bot supports prefix-based commands and slash/interaction commands depending on integrations.

Basic usage

```
!help        # show help
!ping        # respond with pong
!echo hello  # plugin echo replies with `hello`
```

Writing a command plugin

1. Create a plugin module under `plugins/`.
2. Register commands via the plugin API:

```python
from xeno_bot.plugin import Command

def ping(ctx):
    return "pong"

commands = [Command(name="ping", handler=ping)]
```
