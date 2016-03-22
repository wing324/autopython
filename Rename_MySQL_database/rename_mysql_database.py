#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
[INFORMATION]
rename_mysql_database
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
"""

import MySQLdb
import MySQLdb.cursors
import readline
import argparse
import getpass
import re


def parser_options():
	parser = argparse.ArgumentParser(description="Rename mysql database",formatter_class=argparse.ArgumentDefaultsHelpFormatter,conflict_handler="resolve",add_help=True)
	parser.add_argument("--ask-pass", action="store_true", dest="prompt_password", help="Prompt for password")
	parser.add_argument("-c","--create-database",dest="create_new_database",action="store_true",help="Create the new database")
	parser.add_argument("-d","--drop-database",dest="drop_old_database",action="store_true",help="Drop the old database")
	parser.add_argument("-H","--host",dest="host",default="localhost",help="MySQL host")
	parser.add_argument("-n","--new-datase",dest="new_database",required=True,help="The new database name")
	parser.add_argument("-o","--old-database",dest="old_database",required=True,help="The old database name")
	parser.add_argument("-p","--password",dest="password",default='',help="MySQL password")
	parser.add_argument("-P","--port",dest="port",type=int,default=3306,help="TCP/IP port")
	parser.add_argument("-S","--socket",dest="socket",default="/var/run/mysqld/mysql.sock",help="MySQL socket file. Only applies when host is localhost")
	parser.add_argument("-u","--user",dest="user",required=True,help="MySQL user")
	parser.add_argument("-v","--verbose",dest="verbose",default=True,help="Print user friendly messages")
	return parser.parse_args()
# 定义rename_database的参数选项
# define rename_database.py options


def verbose(message):
	if args.verbose:
		print "-- %s" % message


def conn_mysql():
	verbose("Connecting to MySQL......")
	if args.prompt_password:
		password=getpass.getpass("Please input your MySQL password:")
	else:
		password = args.password
	conn = MySQLdb.connect(user=args.user,host=args.host,port=args.port,unix_socket=args.socket,passwd=args.password,db=args.old_database,cursorclass=MySQLdb.cursors.DictCursor)
	return conn
	# 建立MySQL连接
	# connect to MySQL


def rename_database():
	global row_affected
	olddatabase = args.old_database
	newdatabase = args.new_database
	verbose("get tables from old database......")
	command = cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema=%s",olddatabase)
	row_affected=cur.rowcount
	results = cur.fetchall()
	# 获取需要被重命名数据库中的所有表名称
	# get all the table names required to be renamed
	verbose("rename database ......")
	for i in xrange(0,len(results)):
		table = results[i]['table_name']
		command = cur.execute("RENAME TABLE %s.%s TO %s.%s"%(olddatabase,table,newdatabase,table))
		# 循环获取每个表名称,对每个表重命名其数据库名称
		# search each table name to rename


args = parser_options()
mydb = conn_mysql()
cur = mydb.cursor()
try:
	if args.create_new_database:
		command1 = cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name=%s",args.new_database)
		results1 = cur.fetchall()
		if len(results1)>0:
			print "The %s database exists!"%(args.new_database)
		else:
			verbose("Create new database......")
			command2 = cur.execute("CREATE DATABASE %s"%(args.new_database))
		# 创建新的数据库
		# create new database
	else:
		pass
	rename_database()
	print "Total:%s tables are renamed" %(row_affected)
	if args.drop_old_database:
		command3 = cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name=%s",args.old_database)
		results3 = cur.fetchall()
		if len(results3) == 0:
			print "The %s database not exists!"%(args.old_database)
		else:
			verbose("Drop old database......")
			command4 = cur.execute("DROP DATABASE %s"%(args.old_database))
		# 删除旧的数据库
		# drop old database
	else:
		pass
	verbose("Complete!")
except Exception,err:
	verbose("Error!")
	print Exception,err
cur.close()
mydb.close()

