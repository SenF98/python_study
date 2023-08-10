# -*- coding: utf-8 -*-
'''
@File    :   字符串.py
@Time    :   2023/08/09 17:21:49
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''

print(3 * '重要的事情说三遍\n')

word = 'Python'
print(word[0])
# index 0 开始 不包括index2
print(word[0:2])

print(word[-1])  # 输出结果为n 负数索引从右往左  从-1开始 -0 0都是 P

print('word[:2]:' + word[:2])  # 结果是索引0-1的字符串

# python存在索引越界问题 但是切片会自动处理越界索引
print('word[:42]:' + word[:42])
print('word[42:]:' + word[42:])

# python字符串是不能修改的
print('生成一个新的字符串来进行字符串的修改：' + 'J' + word[1:])

# python自带函数len()返回字符串长度
s = 'abcdefghijklmn'
len(s)
#  无法直接打印int值 用.__str__()函数 转换为str
print('字符串s的长度是:' + len(s).__str__())

# 倒序字符串
s = '把这个语句倒过来'
print(s[::-1])