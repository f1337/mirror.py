import json
import sys

class MirrorCLI(object):
    @staticmethod
    def help():
        return 'mirror {push|pull} [--dry] [--config <file>]'



    def __init__(self, argv):
        if len(argv) < 1:
            self.exit(True)

        self.action = argv.pop(0)
        self.config = '~/.config/mirror.py/mirror.json'
        self.dry_run = False

        if self.action in ('pull', 'push'):
            while len(argv) > 0:
                opt = argv.pop(0)
                if opt == '--dry':
                    self.dry_run = True
                elif opt == '--config':
                    if len(argv) > 0:
                        self.config = argv.pop(0)
                else:
                    self.exit(True)
        elif self.action in ('-h', '--help'):
            self.exit()
        else:
            self.exit(True)



    def exit(self, error = False):
        print MirrorCLI.help()
        if error:
            raise SyntaxError(MirrorCLI.help())
