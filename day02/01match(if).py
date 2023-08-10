# -*- coding: utf-8 -*-
'''
@File    :   01match(if).py
@Time    :   2023/08/10 08:50:32
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

