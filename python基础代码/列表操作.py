# -*- coding:utf-8 -*-
# python_version : 2.7.13

# 列表操作


# 切片操作
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 可以用列表生成式str = [a for a in range(16)]
# 或者list1 = list(range(16))
# 或者list1 = range(16)

# 字符串等序列同样可以切片，切片后原序列不变只是创建一个切片的复制
# python索引从0开始
# 切片操作
print list1[-1:]  # 截取最后一个元素
print list1[0:4]  # 截取第一位到第四位的字符
print list1[:]  # 截取字符串的全部字符
print list1[6:]  # 截取第七个字符到结尾
print list1[:-3]  # 截取从头开始到倒数第三个字符之前
print list1[2]  # 截取第三个字符
print list1[::-1]  # 创造一个与原字符串顺序相反的字符串
print list1[-3:-1]  # 截取倒数第三位与倒数第一位之前的字符
print list1[-3:]  # 截取倒数第三位到结尾
print list1[:-5:-3]  # 逆序截取后5位到后三位，每3个取一个，逆向取值
print list1[:8:2]  # 前8个数，每两步取一个

# 列表方法，除了第一个
list1 = [5, 7, 9, 12, 2, 5, 80, 1, 43, 6, 1, 5, 6, 0, 1]

list1.sort()
# 按大小排序，数字按大小，字母比较首字母ascii码
list1 = [5, 7, 9, 12, 2, 5, 80, 1, 43, 6, 1, 5, 6, 0, 1]
list1.reverse()
# 反向排序，并不是按大小反向排，只是倒置顺序
list1.sort(reverse=True)
# 反向排序,按大小从大到小排序，字母比较ascii码
list1.append(9)
# 在列表尾部添加一个元素9
list1.pop()
# 删除最后一个元素
list1.pop(3)
# 删除索引为3的元素
list1.insert(3, 5)
# 在索引为3的位置插入元素5
list1.index(5)
# 返回第一个元素5的索引
list1.count(5)
# 返回统计元素5在列表中出现的次数
list2 = [1, 3]
list1.extend(list2)
# 在list列表尾部加入list2的内容
list1.remove(5)
# 移除索引在前的一个元素5

list1 = [1, 2, 3]
list2 = [3, 4, 5]
list1.extend(list2)
print list1
# 将一个列表添加到一个列表的尾部
# 似乎list = list + list2也能实现


# 列表函数
sorted(list1)
# 返回列表的排序，不会改变list1
len(list1)
# 返回列表的长度，返回元素个数
max(list1)
# 返回列表中的最大值
min(list1)
# 返回列表中的最小值
list(list2)
# 将对象转化为列表
sum(list1)
# 列表元素求和,列表元素必须为数字
print '.'.join(list1)
# 将列表的分隔符换成.并返回字符串，不改变list1
tuple(list1)
# 将列表转换为元组
all(list1)
# 检查所有项是否为True，全是则返回Ture，有一个不是则返回False
any(list1)
# 检查是否有一项为Ture，有一个Ture则返回Ture，全是False则返回False


# 列表语句
del list1[0]
# 删除0索引位置的元素
print 1 in list1
# 判断1是否在list1中，在则返回True不在则返回False
# not in 同理 只是与in相反
for i in list1:
    pass
# 使用i对list1中的元素迭代
list1[0] = 1
# 对列表索引为0的元素重新赋值
list1 = [1, 2, 3, [1, 2, 3]]
# list1[3][2]可以这样选取列表list1的3位置上的列表中的元素

del list1[1:5]
# 删除列表1到5位置的元素
del list1[1:10:2]
# 在列表1到10位置每隔2步删一次



# 列表生成式
# 生成[1,2,3,4,5,6,7,8,9]
print [a for a in range(10)]
# 生成[1x1, 2x2, 3x3, ..., 9x9]
print [x * x for x in range(1, 10)]
# 可以使用两层循环
print [m + n for m in 'ABC' for n in 'DEF']

'''带判断的生成式，isinstance(x,int/float/str)判断x是否为
整数/浮点数/字符串，是返回True否返回Flase，判断类型(还有其他类型)'''
L1 = ['Hello', 'World', 18, 'Apple', None]
# 生成式含义，为在L1中循环，若s为字符串则转换为小写后放入L2
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print L2

# 列表生成器
