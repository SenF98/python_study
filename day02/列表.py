# -*- coding: utf-8 -*-
'''
@File    :   列表.py
@Time    :   2023/08/10 11:05:46
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

# 列表的拼接
items3 = items1 + items2
print(items3)    # [35, 12, 99, 68, 55, 87, 45, 8, 29]
# 列表的重复
items4 = ['hello'] * 3
print(items4)    # ['hello', 'hello', 'hello']
# 列表的成员运算
print(100 in items3)        # False
print('hello' in items4)    # True

# 获取列表的长度(元素个数)
size = len(items3)
print(f'item3长度是{size}')                 # 9
# 列表的索引
print(items3[0], items3[-size])        # 35 35
items3[-1] = 100
print(items3[size - 1], items3[-1])    # 100 100

items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)    # True

items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)    # True
