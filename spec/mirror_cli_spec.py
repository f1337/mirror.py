from expects import *
from mirror.cli import MirrorCLI

with description('MirrorCLI'):



	with context('MirrorCLI.help()'):
		with it('returns the CLI help'):
			expect(
				MirrorCLI.help()
			).to(equal('mirror {push|pull} [--dry] [--config <file>]'))



	with context('MirrorCLI([])'):
		with it('raises SyntaxError'):
			expect(
				lambda: MirrorCLI([])
			).to(raise_error(SyntaxError))


	with context('MirrorCLI(["-h"])'):
		with it('raises SyntaxError'):
			expect(
				lambda: MirrorCLI(['-h'])
			).not_to(raise_error(SyntaxError))


	with context('MirrorCLI(["--help"])'):
		with it('raises SyntaxError'):
			expect(
				lambda: MirrorCLI(['--help'])
			).not_to(raise_error(SyntaxError))


	with context('MirrorCLI(["invalid_action"])'):
		with it('raises SyntaxError'):
			expect(
				lambda: MirrorCLI(['invalid_action'])
			).to(raise_error(SyntaxError))


	with context('MirrorCLI(["pull"])'):
		with before.each:
			self.subject = MirrorCLI(['pull'])

		with it('parses the arguments into properties'):
			expect(self.subject).to(have_properties({
				'action': 'pull',
				'config': '~/.config/mirror.py/mirror.json',
				'dry_run': False
			}));


	with context('MirrorCLI(["push"])'):
		with before.each:
			self.subject = MirrorCLI(['push'])

		with it('parses the arguments into properties'):
			expect(self.subject).to(have_properties({
				'action': 'push',
				'config': '~/.config/mirror.py/mirror.json',
				'dry_run': False
			}));


	with context('MirrorCLI(["pull", "--config", "custom.json"])'):
		with before.each:
			self.subject = MirrorCLI(
				["pull", "--config", "custom.json"]
			)

		with it('parses the arguments into properties'):
			expect(self.subject).to(have_properties({
				'action': 'pull',
				'config': 'custom.json',
				'dry_run': False
			}));


	with context('MirrorCLI(["push", "--dry"])'):
		with before.each:
			self.subject = MirrorCLI(
				["push", "--dry"]
			)

		with it('parses the arguments into properties'):
			expect(self.subject).to(have_properties({
				'action': 'push',
				'config': '~/.config/mirror.py/mirror.json',
				'dry_run': True
			}));


	with context('MirrorCLI(["pull", "--dry", "--config", "custom.json"])'):
		with before.each:
			self.subject = MirrorCLI(
				["pull", "--dry", "--config", "custom.json"]
			)

		with it('parses the arguments into properties'):
			expect(self.subject).to(have_properties({
				'action': 'pull',
				'config': 'custom.json',
				'dry_run': True
			}));


	with context('MirrorCLI(["push", "--config", "custom.json", "--dry"])'):
		with before.each:
			self.subject = MirrorCLI(
				["push", "--config", "custom.json", "--dry"]
			)

		with it('parses the arguments into properties'):
			expect(self.subject).to(have_properties({
				'action': 'push',
				'config': 'custom.json',
				'dry_run': True
			}));
