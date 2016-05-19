#! /usr/bin/env python
# coding:utf-8

def dir_exists(directory):
# 判断文件夹是否存在,存在则跳过,不存在则创建
# If directory exists,skip;else,create directory
  if os.path.exists(directory) == True:
	  pass
  else:
	  os.makedirs(directory)

dir_exists(test_dir)


	
