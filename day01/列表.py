# -*- coding: utf-8 -*-
'''
@File    :   列表.py
@Time    :   2023/08/09 21:31:53
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

# 与字符串不同 列表内容是可变的
cubes = [1, 8, 27, 65, 125]
print('cubes现在是:'+cubes.__str__() + ',第四个值应该是4**3,错误')
cubes[3] = 4 ** 3
print(cubes)