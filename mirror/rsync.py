import json
import os



class Mirror (object):
	def __init__ (self, file):
		with open(os.path.expanduser(file)) as config_json:
			config = json.load(config_json)
			self.command = config['command']
			self.dry_run = False
			self._flags = config['flags']
			self.options = config['options']
			self.local_prefix = config['local_prefix']
			self.remote_prefix = config['remote_prefix']
			self._targets = config['targets']
			self.verbose = False



	def cmd (self, target, paths):
		return ' '.join([
			self.command,
			('-' + self.flags() + target['flags']),
			' '.join(self.options + target['options']),
			paths % {
				'local_prefix': self.local_prefix,
				'remote_prefix': self.remote_prefix,
				'remote': target['remote'],
				'local': target['local']
			}
		])

	def flags (self):
		return (
			self._flags +
			('n' if self.dry_run else '') +
			('v' if self.verbose else '')
		)

	def pull (self, target_name):
		return self.cmd(
			self.target(target_name),
			'%(remote_prefix)s%(remote)s/ %(local_prefix)s%(local)s/'
		)

	def push (self, target_name):
		return self.cmd(
			self.target(target_name),
			'%(local_prefix)s%(local)s/ %(remote_prefix)s%(remote)s/'
		)

	def target (self, key):
		return self._targets[key]

	def targets (self, keys=None):
		keys = keys or self._targets.keys()
		return { k: self.target(k) for k in keys }
