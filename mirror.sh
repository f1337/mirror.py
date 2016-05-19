#! /usr/bin/env python

import os
import sys
from mirror.rsync import Mirror
from mirror.cli import MirrorCLI



def main(argv):
		try:
				cli = MirrorCLI(argv)
				mirror = Mirror(cli.config, cli.dry_run)

				for t in mirror.targets:
						debug = getattr(mirror, cli.action)(t)
						print debug
						os.system(debug)
		except IOError, error:
				print 'Unable to open config file =>', error
		except SyntaxError:
				sys.exit(2)



if __name__ == "__main__":
		main(sys.argv[1:])
