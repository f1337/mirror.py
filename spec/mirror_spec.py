from expects import *
from mirror.rsync import Mirror


with description('Mirror'):



	with context('invalid config file'):
		with before.each:
			self.fixture = 'no-such-file.json'

		with it('raises IOError'):
			expect(lambda: Mirror(self.fixture)).to(raise_error(IOError))



	with context('valid config file'):
		with before.each:
			self.fixture = 'spec/fixtures/config.json'


		with context('dry run'):
			with before.each:
				self.subject = Mirror(self.fixture, True)

			with context('.flags'):
				with it('returns the configured value plus "n"'):
					expect(self.subject.flags).to(equal('rpvn'))


		with context('live run'):
			with before.each:
				self.subject = Mirror(self.fixture)

			with context('.flags'):
				with it('returns the configured value'):
					expect(self.subject.flags).to(equal('rpv'))

			with context('.pull("foo")'):
				with it('returns the remote-to-local rsync command for target "foo"'):
					expect(self.subject.pull('foo')).to(equal(
						'/usr/bin/rsync -rpvlt --delete rsync://bobby@tables.local/foo/ ~/foo/'
					))

			with context('.push("bar")'):
				with it('returns the local-to-remote rsync command for target "bar"'):
					expect(self.subject.push('bar')).to(equal(
						"/usr/bin/rsync -rpv --delete --exclude='.DS_Store' ~/bar/baz/ rsync://bobby@tables.local/bar/baz/"
					))

			with context('.target("foo")'):
				with it('returns the target "foo"'):
					expect(self.subject.target('foo')).not_to(be_none)

			with context('.targets'):
				with it('returns "foo" and "bar" targets *only*'):
					expect(self.subject.targets.keys()).to(equal(
						['foo', 'bar']
					))
