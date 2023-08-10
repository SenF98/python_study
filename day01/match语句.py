# -*- coding: utf-8 -*-
'''
@File    :   match语句.py
@Time    :   2023/08/09 22:28:02
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
#注意最后一个代码块：“变量名” _ 被作为 通配符 并必定会匹配成功。
print(http_error(404))
print(http_error(205))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
var = 2
p = Point(y=var, x=1)
print(p)