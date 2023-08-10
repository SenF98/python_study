# -*- coding: utf-8 -*-
'''
@File    :   match语句2point案例.py
@Time    :   2023/08/09 23:07:08
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''
# TODO __match_args__的含义
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
def check_points(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(x1,y1),Point(x2,y2)]:
            print(f"两个点{x1},{y1}和{x2},{y2}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")
var = 2
p1 = Point(1,2)
p2 = Point(0,3)
check_points([p1,p2])