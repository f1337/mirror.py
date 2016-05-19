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

Copy the sample `mirror.json` to `~/.config/mirror.py/mirror.json` and edit to
your liking.

## Contributing

Submit a pull-request, including unit test coverage.

A `Vagrantfile` has been provided for ease of development.
Vagrant will install `pip` and dev dependencies in an Ubuntu VM:

```
vagrant up
vagrant ssh
cd /vagrant
```

Alternately, install the dev dependencies via `pip`:

```
pip install -r requirements-dev.txt
```

### Testing

```
mamba
```
