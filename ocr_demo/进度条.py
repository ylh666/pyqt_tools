#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 16:15
# @Author  : ylh
# @FileName: 进度条.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Author  : FELIX
# @Date    : 2018/5/17 16:43

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
import sys
import PyQt5.sip
from  QCandyUi import CandyWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
class MyQt(QWidget):##,
    def __init__(self):
        super(MyQt, self).__init__()
        self.initUI()
        #palette = QPalette()
        #palette.setBrush(QPalette.Background, QBrush(QPixmap("gif.gif")))##2000.jpg
        #self.setPalette(palette)
        ###-------------gif背景图片错误-------------##
        movie = self.QMovie('gif.gif')
        # self.labMovies.setMovie(movie)
        # movie.start()
        # movie.setCacheMode(self.QtGui.QMovie.CacheAll)
        # movie.setSpeed(100)
        self.movie_screen.setMovie(movie)
        movie.start()
    def initUI(self):
        # 构建一个进度条
        self.pbar = QProgressBar(self)
        # 从左上角30-50的界面，显示一个200*25的界面
        self.pbar.setGeometry(30, 50, 200, 25)  # 设置进度条的位置
        # 设置开始按钮
        self.btn = QPushButton('开始', self)
        self.btn.move(50, 90)  # 按钮移动的位置
        # 点击按钮
        # 信号函数不能加括号
        self.btn.clicked.connect(self.doAction)


        # 构建一个计时器
        self.timer = QBasicTimer()
        # 计数
        self.step = 0
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('我是进度条')
        # self.setWindowIcon(QIcon('1.jpg'))

        #self.show()

    def doAction(self):
        # 判断是否处于激活状态
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100,self)
            self.btn.setText('停止')
    def timerEvent(self, *args, **kwargs):
        if self.step>=100:
            # 停止进度条
            self.timer.stop()
            self.btn.setText('完成')
            return
        self.step+=1
        # 把进度条每次充值的值赋给进图条
        self.pbar.setValue(self.step)


if __name__ == '__main__':
    # 创建一个Qt应用对象
    app=QApplication(sys.argv)
    myqt=MyQt()
    #myqt = CandyWindow.createWindow(myqt,'bluegreen','progress_bar','favicon.ico')
    # 程序和窗口 --- 一个程序可以有多个窗口
    myqt.show()
    # 当前的程序开始运行
    sys.exit(app.exec_())
