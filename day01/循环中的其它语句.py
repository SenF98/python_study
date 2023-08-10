# -*- coding: utf-8 -*-
'''
@File    :   循环中的其它语句.py
@Time    :   2023/08/09 22:22:13
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''
# 这是循环的else子句 for的子句
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
