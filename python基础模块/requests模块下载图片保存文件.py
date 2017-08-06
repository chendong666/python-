# -*- coding:utf-8 -*-
#__author__ = 'wukong'
# python_version : 2.7.13

import requests
#import urllib
url = 'https://cdn.pixabay.com/photo/2017/08/03/00/34/world-trade-centre-2574316__340.jpg'
#无版权图片
r = requests.get(url)

with open('city.jpg', 'wb') as f:
    f.write(r.content)
#urllib.urlretrieve(url,'city1.jpg')
#使用urllib库的urlretrieve()也可以实现图片下载