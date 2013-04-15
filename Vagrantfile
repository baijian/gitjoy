# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.network :hostonly, "192.168.33.10"
  config.vm.provision Fabric do |fabric|
    fabric.tasks = ["develop"]
  end
end

class Fabric < Vagrant::Provisioners::Base
  class Config < Vagrant::Config::Base
    attr_accessor :fabfile_path
    attr_accessor :fabric_path
    attr_accessor :python_path
    attr_writer :tasks

    def _default_fabfile_path
      File.exist?("fabfile.py") ? "fabfile.py" : "fabfile/__init__.py"
    end

    def _default_fabric_path
      "fab"
    end

    def _default_python_path
      "python"
    end

    def validate(env, errors)


