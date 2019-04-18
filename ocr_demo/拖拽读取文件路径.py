#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 16:19
# @Author  : ylh
# @FileName: 拖拽读取文件路径.py
# @Software: PyCharm

# 爱尚博客——fennbk.com
# By：Fenn
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fennbk_com(QWidget):
    def __init__(self):
        super(Fennbk_com, self).__init__()
        # 窗口标题
        self.setWindowTitle('爱尚博客')
        # 定义窗口大小
        self.resize(500, 400)
        self.QLabl = QLabel(self)
        self.QLabl.setGeometry(0, 100, 4000, 38)
        # 调用Drops方法
        self.setAcceptDrops(True)

    # 鼠标拖入事件
    def dragEnterEvent(self, evn):
        self.setWindowTitle('鼠标拖入窗口了')
        self.QLabl.setText('文件路径：\n' + evn.mimeData().text())
        # 鼠标放开函数事件
        evn.accept()

    # 鼠标放开执行
    def dropEvent(self, evn):
        self.setWindowTitle('鼠标放开了')

    def dragMoveEvent(self, evn):
        print('鼠标移入')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fennbk = Fennbk_com()
    fennbk.show()
    sys.exit(app.exec_())