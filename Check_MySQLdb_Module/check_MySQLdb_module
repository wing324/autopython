#! /usr/bin/env python
# coding:utf-8


'''
[INFORMATION]
Check MySQLdb Module
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

import imp
import os

def check_mysqldb_modules():
# 检查MySQLdb模块是否存在
# check MySQLdb module exists
	try:
		imp.find_module('MySQLdb')
		found = 1
	except ImportError:
		found = 0 
	if found == 0:
		os.system('yum install -y MySQL-python')
		# 如果MySQLdb不存在,则使用yum安装MySQL-python
		# If MySQLdb doesn`t exist, then use Yum to install MySQL-python
	else:
		pass
		# 如果MySLQdb存在,则什么都不用做
		# If MySLQdb exists, there's nothing to do
		
check_mysqldb_modules()
