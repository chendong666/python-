# -*- coding:utf-8 -*-
# python_version : 2.7.13

# python中保留字（即不能随便用作变量名）有如下：
print True
print False
# 布尔值
print True and True
print True and False and True
# and 逻辑与
print True or False
# or 逻辑或
print not False
# not 逻辑非
# print 在屏幕上显示
if False:
    pass
elif False:
    pass
else:
    pass
# 条件判断语句 if elif else,
# 空白语句 pass 即这行为空白
while True:
    pass
# while 当条件正确就一直循环代码块

for i in range(10):
    if i == 3:
        continue
    elif i == 5:
        break
    else:
        print i
# for 循环使i迭代range()中的值
# continue 跳过此次循环
# break结束循环

# del删除
a = ['a', '2', '3']
print a
del a['a']
print a
a = {'a': 1}
print a
del a['a']
print a

# from import as引入模块时使用
from pprint import pprint as p

p([1, 2, 3])

# global nonlocal全局变量与局部变量
pass
pass
pass

# assert断言
assert 1 != 1
assert 1 == 1
# 当后面的表达式返回False就报错
# 在测试代码时较为有用

# with 上下文管理器
pass
pass
pass

#