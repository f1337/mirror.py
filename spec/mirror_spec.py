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
			self.subject = Mirror('spec/fixtures/config.json')


		with context('.flags()'):
			with it('returns the configured value'):
				expect(self.subject.flags()).to(equal('rp'))

		with context('.pull("leg")'):
			with it('returns the remote-to-local command for "leg"'):
				expect(self.subject.pull('leg')).to(equal(
					'/usr/bin/rsync -rplt --delete rsync://bobby@tables.local/my/leg/ ~/my/leg/'
				))

		with context('.push("button")'):
			with it('returns the local-to-remote command for "button"'):
				expect(self.subject.push('button')).to(equal(
					"/usr/bin/rsync -rp --delete --exclude='.DS_Store' ~/button/ rsync://bobby@tables.local/button/"
				))

		with context('.target("leg")'):
			with it('returns the target "leg"'):
				expect(self.subject.target('leg')).not_to(be_none)

		with context('.targets'):
			with it('returns "leg" and "button" targets *only*'):
				expect(
					set(self.subject.targets.keys())
				).to(equal(
					set(['leg', 'button'])
				))


		with context('.dry_run = True'):
			with before.each:
				self.subject.dry_run = True

			with context('.flags()'):
				with it('returns the configured value plus "n"'):
					expect(self.subject.flags()).to(equal('rpn'))


		with context('.verbose = True'):
			with before.each:
				self.subject.verbose = True

			with context('.flags()'):
				with it('returns the configured value plus "v"'):
					expect(self.subject.flags()).to(equal('rpv'))
