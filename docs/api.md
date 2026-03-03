# API Reference

This section contains the high-level API for plugin authors.

Core classes

- `Plugin`: base class for plugins
- `Command`: represents a command, with `name`, `handler`, and `help`
- `Context`: runtime context passed to handlers containing `message`, `user`, and `send()` helper

Example: simple plugin

```python
from xeno_bot.plugin import Plugin, Command

class EchoPlugin(Plugin):
    def setup(self):
        self.add_command(Command("echo", self.echo))

    def echo(self, ctx, *args):
        return " ".join(args)
```
