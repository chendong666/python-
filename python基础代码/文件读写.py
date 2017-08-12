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
print '>>>>>>>>>>>>>>二进制>>>>>>>>>>'
with open('aa.txt', 'rb+') as f:
    print f.read()

    # 还有其他打开方式
    # 't'文本模式
    #  'b'二进制模式
    #  不能以'b'或者‘+’开头
    #  'r+ '可读写方式
    #  'w+' 可读写方式
    #  'a+' 附加可读写
    #  'rb+'二进制可读写
    #  'wb+'二进制读写
    #  'ab+'附件二进制读写
