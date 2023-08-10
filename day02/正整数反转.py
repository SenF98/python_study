# -*- coding: utf-8 -*-
'''
@File    :   正整数反转.py
@Time    :   2023/08/10 09:05:50
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

# 方法一 看做字符串 进行反转
a = 12345
reversed_num = 0
reversed_num = int(a.__str__()[::-1])
print(reversed_num)

# 方法二 循环法
reversed_num = 0
while a > 0:
    reversed_num = reversed_num*10 + a % 10
    a //= 10
print(reversed_num)