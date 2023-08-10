# -*- coding: utf-8 -*-
'''
@File    :   for语句.py
@Time    :   2023/08/09 21:53:17
@Author  :   sen98
@Version :   1.0
@Site    :
@Desc    :   None
'''
'''
Python 的 for 语句与 C 或 Pascal 中的不同。
Python 的 for 语句不迭代算术递增数值（如 Pascal），
或是给予用户定义迭代步骤和暂停条件的能力（如 C），
而是迭代列表或字符串等任意序列，元素的迭代顺序与在序列中出现的顺序一致。
'''
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# 遍历集合时修改集合内容，会生成错误的结果，应遍历该集合的副本或者创建新的集合
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# range()函数 生成的不包括终止数值
for i in range(5):
    print(i)

# range(10) 生成 10 个值，这是一个长度为 10 的序列，其中的元素索引都是合法的。
# range 可以不从 0 开始，还可以按指定幅度递增（递增幅度称为 '步进'，支持负数）
a = list(range(5, 10))
print(a)
b = list(range(0, 10, 3))
c = list(range(-10, -100, -30))
print(b)
print(c)

# sum() 是一种把可迭代对象作为参数的函数
print('和为' + sum(range(4)).__str__())
