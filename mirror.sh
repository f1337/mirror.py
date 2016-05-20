#! /usr/bin/env python

import argparse
import os
import sys

from mirror import __version__
from mirror.rsync import Mirror



def main ():
	arguments = _parse_arguments()

	if arguments.verbose:
		print "arguments:", vars(arguments)

	try:
		mirror = Mirror(arguments.config)
	except IOError, error:
		print 'Unable to open config file =>', error
		sys.exit(2)

	mirror.dry_run = arguments.dry_run
	mirror.verbose = arguments.verbose

	try:
		for t in mirror.targets(arguments.target):
			command = getattr(mirror, arguments.action)(t)
			if arguments.verbose:
				print command
			os.system(command)
	except KeyError, error:
		print 'Invalid target: %s. Valid values: %s' % (error, ', '.join(mirror.targets().keys()))
		sys.exit(2)


def _parse_arguments ():
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'--version',
		default=False,
		action='version',
		version=__version__
	)

	parser.add_argument(
		'action',
		choices=['pull', 'push'],
		help='"pull": remote to local or "push": local to remote'
	)
	parser.add_argument(
		'target',
		nargs='*',
		help='Target(s) to sync (default: all configured targets)'
	)
	parser.add_argument(
		'-n',
		'--dry',
		action='store_true',
		default=False,
		dest='dry_run',
		help='Dry run (do not transfer any files)'
	)
	parser.add_argument(
		'-v',
		'--verbose',
		default=False,
		action='store_true',
		help='Print debug output (noisy)'
	)
	parser.add_argument(
		'--config',
		action='store',
		default='~/.config/mirror.py/mirror.json',
		help='Configuration file (default: %(default)s)'
	)

	return parser.parse_args()



if __name__ == "__main__":
	main()
