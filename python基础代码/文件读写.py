# -*- coding:utf-8 -*-
# python_version : 2.7.13

print '>>>>>>>>>>>>>>只写打开，没有该文件就会创建文件>>>>>>>'
with open('aa.txt', 'w') as f:
    # with 上下文管理器
    f.write("I\tlove\tPython!\nIt's funny.")

print '>>>>>>>>>>>>>>附加写打开，没有同样会创建文件>>>>>>>>>'
with open('aa.txt', 'a') as f:
    f.write('\npython2.7.13')

print '>>>>>>>>>>>>>>只读打开，没有就报错>>>>>>>>>>>>>>>>>>>'
print '(1)全部读取'
with open('aa.txt', 'r') as f:
    print f.read()
print '(2)读取一行'
with open('aa.txt', 'r') as f:
    print f.readline()
print '(3)按行读取'
with open('aa.txt', 'r') as f:
    print f.readlines()

print '>>>>>>>>>>>>>>>再次只写打开会清空文件>>>>>>>>>>>>>>>>>'
with open('aa.txt', 'w') as f:
    pass
