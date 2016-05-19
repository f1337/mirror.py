import unittest
from mirror import Mirror

class MirrorTest(unittest.TestCase):
    def setUp(self):
        self.subject = Mirror('mirror_test.json')


    def test_init_with_missing_config_file_raises_exception(self):
        with self.assertRaises(IOError):
            subject = Mirror('no-such-file.json')

    def test_flags(self):
        self.assertEqual('rpv', self.subject.flags)

    def test_flags_dry_run(self):
        subject = Mirror('mirror_test.json', True)
        self.assertEqual('rpvn', subject.flags)

    def test_pull(self):
        self.assertEqual('/usr/bin/rsync -rpvlt --delete rsync://bobby@tables.local/foo/ ~/foo/', self.subject.pull('foo'))

    def test_push(self):
        self.assertEqual("/usr/bin/rsync -rpv --delete --exclude='.DS_Store' ~/bar/baz/ rsync://bobby@tables.local/bar/baz/", self.subject.push('bar'))

    def test_target(self):
        self.assertIsNotNone(self.subject.target('foo'))

    def test_targets(self):
        self.assertListEqual(['foo', 'bar'], self.subject.targets.keys())



if __name__ == '__main__':
    unittest.main()
