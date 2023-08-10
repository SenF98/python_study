# -*- coding: utf-8 -*-
"""
@File    :   元组.py
@Time    :   2023/08/10 14:05:12
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
"""

# 元组是不可变类型 意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能进行修改。
t1 = (30, 10, 55)
t2 = ('sen', 40, True, '安徽芜湖')
print(type(t1), type(t2))
print(100 in t1)    # False
print(40 in t2)     # True

# 拼接
t3 = t1 + t2
print(t3)           # (30, 10, 55, '骆昊', 40, True, '四川成都')

# 切片
print(t3[::3])      # (30, '骆昊', '四川成都')

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (30, 11, 55))    # True

# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>