import unittest
from mirror_cli import MirrorCLI

class MirrorCLITest(unittest.TestCase):

    def test_help(self):
        self.assertEqual('mirror {push|pull} [--dry] [--config <file>]', MirrorCLI.help())

    def test_arguments_empty(self):
        with self.assertRaises(SyntaxError):
            subject = MirrorCLI([])

    def test_action_h(self):
        subject = MirrorCLI(['-h'])

    def test_action_help(self):
        subject = MirrorCLI(['--help'])

    def test_action_invalid(self):
        with self.assertRaises(SyntaxError):
            subject = MirrorCLI(['crack'])

    def test_action_pull(self):
        subject = MirrorCLI(['pull'])
        self.assertEqual('pull', subject.action)

    def test_action_push(self):
        subject = MirrorCLI(['push'])
        self.assertEqual('push', subject.action)

    def test_config(self):
        subject = MirrorCLI('pull --config no-such-file.json'.split(' '))
        self.assertEqual('pull', subject.action)
        self.assertEqual('no-such-file.json', subject.config)

    def test_config_default(self):
        subject = MirrorCLI(['pull'])
        self.assertEqual('~/.config/mirror.py/mirror.json', subject.config)

    def test_dry_run(self):
        subject = MirrorCLI('push --dry'.split(' '))
        self.assertEqual('push', subject.action)
        self.assertEqual(True, subject.dry_run)

    def test_dry_run_default(self):
        subject = MirrorCLI(['push'])
        self.assertEqual(False, subject.dry_run)

    def test_options_reverse_order(self):
        subject = MirrorCLI('pull --config no-such-file.json --dry'.split(' '))
        self.assertEqual('pull', subject.action)
        self.assertEqual('no-such-file.json', subject.config)
        self.assertEqual(True, subject.dry_run)




if __name__ == '__main__':
    unittest.main()
