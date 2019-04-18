#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 19:40
# @Author  : ylh
# @FileName: 提取网页链接URL.py
# @Software: PyCharm
import re
c = open(r'./1.txt',encoding='utf8').readlines()
print(c[1])
print(re.findall(re.compile(r'[\u4e00-\u9fa5]+'),'fsadfs万丹琦真漂亮fsadfad。/'))
# print(c)
# for i in c:
# r = re.finditer(re.compile(r' (http:.*?) '),c[1])
# for i in r:
#     print(i.group(0))
# print(r)
# open(r'./get_url_demo.txt','w').write(str(r))
# s = '2019-03-26T05:00:33.790Z   200      29342 http://ci.hfut.edu.cn/_upload/site/00/75/117/logo.png E http://ci.hfut.edu.cn/3954/list.htm image/png #011 20190326050033762+17 sha1:BTFZWBTPMFRWW47SVVKJWSOWATD4TMIO - -'
# r = re.findall(re.compile(r' (http:.*?) '),s)
# print(r)