#! /usr/bin/env python
# coding:utf-8

'''
[INFORMATION]
Send Email With Python
AUTHOR : Wing
GitHub : https://github.com/wing324
Email : wing324@126.com
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def send_mail(to_email,message):
# 定义邮件发送
# Define send_mail() function
	smtp_host = 'smtp.xxx.com'
	# 发件箱服务器
	# Outbox Server
	from_email = 'from_email@xxx.com'
	# 发件邮箱
	# from_email
	passwd = 'xxxxxx'
	# 发件邮箱密码
	# from_email_password
	msg = MIMEText(message,'plain','utf-8')
	msg['Subject'] = Header(u'Email Subject','utf-8').encode()
	# 邮件主题
	# Email Subject
	smtp_server = smtplib.SMTP(smtp_host,25)
	# 发件服务器端口
	# Outbox Server Port
	smtp_server.login(from_email,passwd)
	smtp_server.sendmail(from_email,[to_email],msg.as_string())
	smtp_server.quit()

send_mail('to_email@xxx.co','Email Context')
# 发送邮件('收件邮箱','邮件正文内容')
# send_mail('to_email','Email Context')
