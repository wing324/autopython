#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
[INFORMATION]
Install  Multiple Instances of MySQL
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

'''
[NOTES]
1. OS : CentOS
2. MySQL configure file is /etc/my.cnf
3. Before runing this script,you must make clean the installation directory of MySQL instance
'''

import readline
import ConfigParser
import os
import fileinput


mysql_installdir = raw_input('please input MySQL install directory,example /data/mysql:')

portlist = []
mysql_num = int(raw_input('please input the number of MySQL instance:'))
for i in range(1,mysql_num+1):
	mysql_port = raw_input('please input the port of instance in sequence,the delimiter is Enter:')
	portlist.append(mysql_port)

for p in portlist:
	os.makedirs('%s/mysqldata%s/binlog'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/innodb_ts'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/innodb_log'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/log'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/mydata'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/relaylog'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/sock'% (mysql_installdir,p))
	os.makedirs('%s/mysqldata%s/tmpdir'% (mysql_installdir,p))
	# Create the installation directory of MySQL instance
	os.system('chown -R mysql:mysql %s' % mysql_installdir)
	# Change the installation directory of MySQL instance privileges
	for line in fileinput.input('/etc/my.cnf',backup='bak',inplace=1):
		print line.replace('[mysqld%s]' % p,'[mysqld]'),
	fileinput.close()
	# change [mysqld3306] to [mysqld] in my.cnf file 
	os.system('mysql_install_db --user=mysql --datadir=%s/mysqldata%s/mydata/ --defaults-file=/etc/my.cnf' %(mysql_installdir,p))
	# install MySQL instance
	for line in fileinput.input('/etc/my.cnf',backup='bak',inplace=1):
		print line.replace('[mysqld]','[mysqld%s]' % p),
	fileinput.close()
	# change [mysqld] to [mysqld3306] in my.cnf file
