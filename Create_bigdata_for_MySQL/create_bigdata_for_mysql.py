#! /usr/bin/env python
# coding:utf-8


'''
[INFORMATION]
Create Big Data For MySQL
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

'''
[NOTES]
1. OS: CentOS.
2. The data type only for number type or string type.
3. Must install MySQL-python module, the install command is 'yum install -y MySQL-python'.
'''

'''
[USAGE]
1. Change the information for connect to MySQL :  conn=MySQLdb.connect(host='localhost',user='root',passwd='',unix_socket='/data/mysql/mysqldata3306/sock/mysql.sock',db='test',charset='utf8').
2. Change the strunct of table :  cur.executemany("insert into t1(id,name,score) values(%s,%s,%s)",values).
3. the 'i' is for the number of auto_increment.
4. The 'random_str()' function produce random string(the length is randomlength),the 'random_num()' function produce random number(the range default from 1 to 100, you can change it in 'random.randint(1,100)').
'''

import MySQLdb
import random
import string
import readline


def random_str(randomlength):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    rdm = random.Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def random_num():
	no = random.randint(1,100)
	return no

try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='',unix_socket='/data/mysql/mysqldata3306/sock/mysql.sock',db='test',charset='utf8')
	cur=conn.cursor()
	lines = int(raw_input('please input the number you want to insert : '))
	start = int(raw_input('please input the min value of auto_increment : '))
	end = start + lines
	randomlength = int(raw_input('please input the length of random string : '))
	values = []
	for i in range(start,end):
		var=random_str(randomlength)
		num = random_num()
		data = (i,var,num)
		values.append(data)
	cur.executemany("insert into t1(id,name,score) values(%s,%s,%s)",values)
	conn.commit()
	cur.close()
	conn.close()

except MySQLdb.Error,err_msg:
	print 'MySQL error massage:',err_msg
