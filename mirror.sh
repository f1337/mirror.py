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
		return

	mirror.dry_run = arguments.dry_run
	mirror.verbose = arguments.verbose

	for t in mirror.targets:
		command = getattr(mirror, arguments.action)(t)
		if arguments.verbose:
			print command
		os.system(command)


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
		help="'pull' to sync from remote to local; 'push' to sync local to remote"
	)
	# parser.add_argument(
	# 	'target',
	# 	default=':default',
	# 	nargs='*',
	# 	help='Target(s) to sync (default: %(default)s)'
	# )
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
