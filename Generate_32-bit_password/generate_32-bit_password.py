#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
使用方式：python generate_32-bit_password.py
'''

import string
import random

# 随机生成32位数字+字母密码
pass_char = string.letters+string.digits
pass_word = random.sample(pass_char,32)
print ''.join(pass_word)
