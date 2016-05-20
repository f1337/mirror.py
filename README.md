# mirror.py
A simple rsync mirroring tool. JSON configuration. Written in Python.

## Usage

```
usage: mirror.sh [-h] [--version] [-n] [-v] [--config CONFIG]
                 {pull,push} [target [target ...]]

positional arguments:
  {pull,push}      "pull": remote to local or "push": local to remote
  target           Target(s) to sync (default: all configured targets)

optional arguments:
  -h, --help       show this help message and exit
  --version        show program's version number and exit
  -n, --dry        Dry run (do not transfer any files)
  -v, --verbose    Print debug output (noisy)
  --config CONFIG  Configuration file (default:
                   ~/.config/mirror.py/mirror.json)
```

### Examples

Push local changes to remote:

```
mirror.sh push
```

Pull local changes from remote:

```
mirror.sh pull
```

Preview changes before pushing or pulling:

```
mirror.sh pull --dry --verbose
mirror.sh push -nv
```

List changed files as they are transferred:

```
mirror.sh pull -v
mirror.sh push --verbose
```

### Configuration

Two sample configurations are provided in [examples](examples). Copy one to `~/.config/mirror.py/mirror.json` and customize to your liking:

* `mirror_rsync_example.json` demonstrates how to configure the script to run `rsync` using the `rsync` network protocol.
* `mirror_ssh_example.json` demonstrates how to configure the script to run `rsync` using the `ssh` network protocol.


## Contributing

Contributions are welcome! Please submit a pull-request, including unit test coverage.

### Development Environment

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
