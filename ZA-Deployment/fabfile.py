#!/usr/bin/env python
from fabric.api import *

#list of IP addresses of hosts
#env.hosts = ['192.168.47.128'] 
env.hosts = ['192.168.47.129']

def enable_repo():
    #ubuntu repo
    run("wget wget http://repo.zabbix.com/zabbix/3.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.4-1%2Bbionic_all.deb")
    run("dpkg -i zabbix-release_3.4-1+xenial_all.deb")
    
    #RHEL Repo
    #run("rpm -ivh https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm")

    
def install_zabbix_agent():
    sudo("apt-get update")
    sudo("apt-get install zabbix-agent")
    #sudo("yum update -y")
    #sudo("yum install zabbix zabbix-agent -y")


def configure_agent():
    put("zabbix_agentd.conf", "/tmp/")
    run("mv /tmp/zabbix_agentd.conf /etc/zabbix/")

def start_zabbix_agent():
    sudo("sudo systemctl start zabbix-agent")



        


    
    
