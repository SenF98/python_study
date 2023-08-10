# -*- coding: utf-8 -*-
'''
@File    :   找素数.py
@Time    :   2023/08/10 09:09:01
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

for num in range(2, 100):
    for factor in range(2, num):
        if num % factor == 0:
            break
    else:
        print(f'这是一个素数' + num.__str__())

# 原版查素数
for num in range(2, 100):
    # 假设num是素数
    is_prime = True
    # 在2到num-1之间找num的因子
    for factor in range(2, num):
        # 如果找到了num的因子，num就不是素数
        if num % factor == 0:
            is_prime = False
            break
    # 如果布尔值为True在num是素数
    if is_prime:
        print(num)