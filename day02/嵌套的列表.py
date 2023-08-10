# -*- coding: utf-8 -*-
'''
@File    :   嵌套的列表.py
@Time    :   2023/08/10 14:01:18
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

scores = [[0] * 3] * 5
print(scores)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
scores[0][0] = 95
print(scores)    #[[95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0]]
# 不能用[[0] * 3] * 5]这种方式来创建嵌套列表

scores = [[0]*3 for _ in range(5)]
scores[0][0] = 95
print(scores)