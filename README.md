# mirror.py
A simple rsync mirroring tool. JSON configuration. Written in Python.

## Usage

```
mirror pull --dry
mirror pull
mirror push --dry
mirror push
```

### Options

* `--dry` for a dry-run (no files will be transferred)
* `--config <file>` to specify the config file (default: `~/.config/mirror.py/mirror.json`)

### Configure

Copy the sample `mirror.json` to `~/.config/mirror.py/mirror.json` and edit to your liking.
