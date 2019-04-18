#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 13:01
# @Author  : ylh
# @FileName: pagerank_demo.py
# @Software: PyCharm
D = 0.85###阻尼系数：在任意时刻，用户到达某页面后并继续向后浏览的概率
index_url=''
import requests
import re
def pagerank(array):
    a = requests.session()
    for i in array:
        con = a.get(url = i).text
        r = re.findall(re.compile(r'"(http:.*?)"'),con)
        print(r)


