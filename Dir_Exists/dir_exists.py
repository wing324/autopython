#! /usr/bin/env python
# coding:utf-8

'''
[INFORMATION]
Directory Exists
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

def dir_exists(directory):
# 判断文件夹是否存在,存在则跳过,不存在则创建
# If directory exists,skip;else,create directory
  if os.path.exists(directory) == True:
	  pass
  else:
	  os.makedirs(directory)

dir_exists(test_dir)


	
