# -*- coding:utf-8 -*-
# python_version:2.7.13

# 转义字符指使原字符表示其他作用,在原字符前加\
# \续行符
'a' \
'b'
# \\在字符串中表示反斜杠（由于python中\用于转义所以输入反斜杠需要输入\\）
print '\\'
# \' 表示 ' 用于防止字符串在此处结尾
print 'a\'b'
# \" 作用同上
print 'a\"b'
# \a bell发出声音
print '\a'
# \b 退格符
print 'aaa\bccc'
# 会显示aaccc
# \0 Null空值
print '\0'
# \n 换行符
print 'a\nb'
# \t 水平制表符
print 'a\tb'
print 'aaa\tb'
# \f 换页符
print 'a\fb'

# 格式化数据
# 格式如下语句后面的%号可以接变量，即格式化变量代表的数据
print 'a%s' % 'aa'
# %d 格式化整数
# %f 格式化浮点数
# %s 格式化字符串
# %+数字+格式化类型即在格式化的字符前加几个空格
# %.+数字+f 即格式化浮点数到几位小数

# 还有部分高级用法，以后更新








