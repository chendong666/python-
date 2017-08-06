# -*- coding:utf-8 -*-
#__author__ = 'wukong'
# python_version : 2.7.13

str = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#可以用列表生成器str = [a for a in range(16)]

#字符串等序列同样可以切片，切片后原序列不变只是创建一个切片的复制
#python索引从0开始
print str[-1:]      # 截取最后一个元素
print str[0:4]      # 截取第一位到第四位的字符
print str[:]        # 截取字符串的全部字符
print str[6:]       # 截取第七个字符到结尾
print str[:-3]      # 截取从头开始到倒数第三个字符之前
print str[2]        # 截取第三个字符
print str[::-1]     # 创造一个与原字符串顺序相反的字符串
print str[-3:-1]    # 截取倒数第三位与倒数第一位之前的字符
print str[-3:]      # 截取倒数第三位到结尾
print str[:-5:-3]   # 逆序截取后5位到后三位，每3个取一个，逆向取值
print str[:8:2]     # 前8个数，每两步取一个
