# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
	config.vm.box = "ubuntu/trusty64"

	config.ssh.forward_agent = true

	config.vm.provision "pip", type: "shell", inline: <<-SHELL
		apt-get update
		apt-get install -yq python-pip
	SHELL

	config.vm.provision "mamba", type: "shell", inline: <<-SHELL
		pip install -r /vagrant/requirements-dev.txt
	SHELL

	config.vm.provision "profile", type: "shell", privileged: false, inline: <<-SHELL
		echo 'alias ll="ls -la"' >> ~/.profile
	SHELL

end
