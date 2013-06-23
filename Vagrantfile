# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.network :hostonly, ip: "192.168.33.10"
    
    config.vm.provision :chef_solo do |chef|
        chef.log_level = :debug
        chef.cookbooks_path = "cookbooks"
        chef.add_recipe("locale")
    end
end
