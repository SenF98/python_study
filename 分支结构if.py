# -*- coding: utf-8 -*-
'''
@File    :   分支结构if.py
@Time    :   2023/08/09 16:24:52
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

username = input('请输入用户名:')
password = input('请输入密码:')
if username == 'admin' and password == '123456':
	print('身份验证成功!')
else:
	print('身份验证失败!')
