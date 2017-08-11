# -*- coding:utf-8 -*-
# python_version:2.7.13

import pprint

# 用于格式化输出数据结构
# 当数据输出过长等回分行等是格式较为整齐
a = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
     'abbbbbbbbb', (1, 2, 4), 5]
pprint.pprint(a)
print a
