# coding: utf-8
'''
@File    :   运算符.py
@Time    :   2023/08/09 16:03:28
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''
import os
a = 2
b = 5
a *= b+5
print(a)

c = b / a
print(f"/符号总是返回浮点数:b / a = {c}")
c = 45 // 20
print("使用//进行整除:%d" % c)

# **计算乘方
print(5 ** 2)
# 2的4次方 结果是16
print(2 ** 4)

print('c:\tovelo\tools')
#不想转义 在引号前加 r
print(r'c:\tovelo\tools')

print(r'hello\'world')

print(r'C:\this\will\work')
print(os.path.join(r'C:\this\will\work', ''))