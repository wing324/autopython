#! /usr/bin/env python
# coding:utf-8

'''
[INFORMATION]
Check MySQLdb Module
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

import os
import time

log_dir = '/usr/local/script/log'
os.chdir(log_dir)
try:
	fileinfo = os.stat(r'error.log')
	filetm = time.localtime(fileinfo.st_mtime)
	filedt = time.strftime('%Y-%m-%d',filetm)
	# 获取日志最后修改的日期
	# Get the last modify date of the log
	curdt = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	# 获取今天的日期
	# Get current date
	if filedt == curdt:
		pass
	else:
		new_name = ('error-%s.log'%(filedt))
		os.rename('error.log',new_name)
	# 对比文件最后修改日期与今天日期
	# Compare the last modify date of the log with current date
except OSError:
	pass
# 为今天之前的日志添加日期后缀
# Rename the log with the suffix date before current date
