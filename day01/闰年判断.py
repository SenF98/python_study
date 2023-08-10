# -*- coding: utf-8 -*-
'''
@File    :   闰年判断.py
@Time    :   2023/08/09 16:20:24
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

year = int(input('请输入年份'))
# 比较运算符会产生布尔值
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)