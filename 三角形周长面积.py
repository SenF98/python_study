# -*- coding: utf-8 -*-
'''
@File    :   三角形周长面积.py
@Time    :   2023/08/09 16:31:07
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长: {peri}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')