# -*- coding:utf-8 -*-
# python_version : 2.7.13

# python中保留字（即不能随便用作变量名）有如下：
print True
print False
# 布尔值
print True and True
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
