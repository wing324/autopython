#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
[INFORMATION]
Install MySQL With RPM
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

'''
[NOTES]
1. Before running this script , you must uninstall the packet of MySQL or MariaDB
2. Make sure that only MySQL RPM packet start with 'MySQL' and end with '.rpm' in MySQL RPM packet directory
3. OS : CentOS
'''


import readline
import os
import glob

if os.system('groups mysql')==0:
	pass
else:
	os.system('groupadd mysql')
	os.system('useradd -g mysql mysql')
# Check the exists of MySQL user and group ,if yes ,skip the reset of the script,otherwise ,execute the reset of script

os.system('yum install -y perl-Module-Install.noarch libaio')
# Install MySQL dependent packet

rpmdir = raw_input('please input MySQL RPM packet absolute path:')
rpmpath = rpmdir + '/MySQL-*.rpm'
rpml = glob.glob(rpmpath)
# Find MySQL RPM packet

for rpmpack in rpml:
	os.system('rpm -ivh '+rpmpack)
# Install MySQL RPM packet
