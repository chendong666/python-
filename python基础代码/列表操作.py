# -*- coding:utf-8 -*-
#__author__ = 'wukong'
# python_version : 2.7.13

list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#可以用列表生成式str = [a for a in range(16)]

#字符串等序列同样可以切片，切片后原序列不变只是创建一个切片的复制
#python索引从0开始
#切片操作
print list[-1:]      # 截取最后一个元素
print list[0:4]      # 截取第一位到第四位的字符
print list[:]        # 截取字符串的全部字符
print list[6:]       # 截取第七个字符到结尾
print list[:-3]      # 截取从头开始到倒数第三个字符之前
print list[2]        # 截取第三个字符
print list[::-1]     # 创造一个与原字符串顺序相反的字符串
print list[-3:-1]    # 截取倒数第三位与倒数第一位之前的字符
print list[-3:]      # 截取倒数第三位到结尾
print list[:-5:-3]   # 逆序截取后5位到后三位，每3个取一个，逆向取值
print list[:8:2]     # 前8个数，每两步取一个



#列表方法，除了第一个
list = [5,7,9,12,2,5,80,1,43,6,1,5,6,0,1]
sorted(list)
#暂时性排序，不会改变list
list.sort()
#按大小排序，数字按大小，字母比较首字母ascii码
list = [5,7,9,12,2,5,80,1,43,6,1,5,6,0,1]
list.reverse()
#反向排序，并不是按大小反向排，只是倒置顺序
list.sort(reverse=True)
#反向排序,按大小从大到小排序，字母比较ascii码
list.append(9)
#在列表尾部添加一个元素9
list.pop()
#删除最后一个元素
list.pop(3)
#删除索引为3的元素
list.insert(3,5)
#在索引为3的位置插入元素5
list.index(5)
#返回第一个元素5的索引
list.count(5)
#返回统计元素5在列表中出现的次数
list2 = [1,3]
list.extend(list2)
#在list列表尾部加入list2的内容
list.remove(5)
#移除索引在前的一个元素5

#列表生成式
#生成[1,2,3,4,5,6,7,8,9]
print [a for a in range(10)]
# 生成[1x1, 2x2, 3x3, ..., 9x9]
print [x * x for x in range(1, 10)]
# 可以使用两层循环
print [m + n for m in 'ABC' for n in 'DEF']

'''带判断的生成式，isinstance(x,int/float/str)判断x是否为
整数/浮点数/字符串，是返回True否返回Flase，判断类型(还有其他类型)'''
L1 = ['Hello', 'World', 18, 'Apple', None]
#生成式含义，为在L1中循环，若s为字符串则转换为小写后放入L2
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print L2

#列表生成器