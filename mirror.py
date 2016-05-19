import json



class Mirror(object):
    @staticmethod
    def help():
        return 'sync.py {push|pull} [--dry]'



    def __init__(self, file, dry_run = False):
        with open(file) as config_json:
            config = json.load(config_json)
            self.command = config['command']
            self.flags = config['flags'] + ('n' if dry_run else '')
            self.options = config['options']
            self.local_prefix = config['local_prefix']
            self.remote_prefix = config['remote_prefix']
            self.targets = config['targets']



    def cmd(self, target, paths):
        return ' '.join([
            self.command,
            ('-' + self.flags + target['flags']),
            ' '.join(self.options + target['options']),
            paths % {
                'local_prefix': self.local_prefix,
                'remote_prefix': self.remote_prefix,
                'remote': target['remote'],
                'local': target['local']
            }
        ])

    def pull(self, target_name):
        return self.cmd(self.target(target_name), '%(remote_prefix)s%(remote)s/ %(local_prefix)s%(local)s/')

    def push(self, target_name):
        return self.cmd(self.target(target_name), '%(local_prefix)s%(local)s/ %(remote_prefix)s%(remote)s/')

    def target(self, key):
        return self.targets[key]
