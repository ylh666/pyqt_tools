#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 21:45
# @Author  : ylh
# @FileName: ocr_qt1.py
# @Software: PyCharm
from ocr import *
from QCandyUi import *
from PyQt5 import sip
#@colorful('blueGreen')
import sys
sys.path.append(r'F:\A大三下\ctf\ocr_demo/截图界面.py')##添加其他文件路径方便识别
sys.path.append(r'F:\A大三下\ctf\ocr_demo/设置按钮样式.qss')
from ocr_demo.截图界面 import *
import keyboard
class MyWindow(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.comboBox.addItem('中文')##单独添加条目
        self.comboBox.addItem('英文')
        # self.comboBox.addItems(['中文','英文'])###数组添加多个条目
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        # self.timer = QtCore.QBasicTimer()
        # self.step = 0
        self.progressBar.setValue(100)
        self.setWindowOpacity(0.9)  ##设置窗口透明度
        self.setWindowIcon(QtGui.QIcon('favicon.ICO'))##改界面的图标
        self.path='./shortscreen.jpg'
        ##-----------背景设置------------##

        # 调用Drops方法
        self.setAcceptDrops(True)
        ##调用keyboard库，suppress如果是True的话，那就是对系统热键进行阻塞
        keyboard.add_hotkey('ctrl+alt+a',self.pushButton_4.click,suppress=True)
        keyboard.add_hotkey('enter',self.pushButton_2.click,suppress=False)
        ##调用剪切板
        self.cb = QtWidgets.QApplication.clipboard()
        ##字体
        # self.textEdit.setStyleSheet("color:red,font-family:楷体")
        # self.textEdit.setStyleSheet("font:red; font-size:20px; color: rgb(241, 70, 62); background-color: green")
        self.textEdit.setStyleSheet("font:black; font-size:19px; color: rgb(0, 0, 0); background-color: white;font-family:楷体")
        self.setAttribute(Qt.WA_StyledBackground)##如果没有显示的话，添加上这句话
        # print(self.textEdit)

    def selectionchange(self, i):
        # 标签用来显示选中的文本
        # currentText()：返回选中选项的文本
        self.textEdit.setText('选择识别语言为：'+self.comboBox.currentText())###setText
        print(self.comboBox.currentText())
        # print('Items in the list are:')
        # 输出选项集合中每个选项的索引与对应的内容
        # count()：返回选项集合中的数目
        # for count in range(self.comboBox.count()):
        #     print('Item' + str(count) + '=' + self.comboBox.itemText(count))
        #     print('current index', i, 'selection changed', self.comboBox.currentText())

    def read_file(self):
        file_name,ok=QFileDialog.getOpenFileName(self,'读取','./')
        if ok:
            self.lineEdit.setText(str(file_name))
            self.textEdit.setText('文件来源：'+str(file_name)+'\n')
        self.path = str(file_name) ###路径名
    def ocr_fenxi(self):
        import pytesseract as p
        from PIL import Image
        # p.pytesseract.tesseract_cmd='E:/A_Ctf_Tool/Tesseract-OCR/tesseract.exe'
        p.pytesseract.tesseract_cmd = 'E:/A_Ctf_Tool/Tesseract-OCR/tesseract.exe '
        if self.comboBox.currentText()=='中文':
            text = p.image_to_string(Image.open(self.path), lang='chi_sim')
        else:
            text = p.image_to_string(Image.open(self.path))
            # print(text)
        self.textEdit.setText(text)
        print(text)
        self.cb.setText(text)
    def cancel(self):
        quit()


    def progress_bar(self,event):
        # if self.step >= 100:
        #     self.timer.stop()
        #     return
        import time
        while self.step != 100:
            time.sleep(0.05)
            self.step += 1
            self.progressBar.setValue(self.step)  ##一般是文件数量较多的时候显示的，setvalue 比较重要

    # 鼠标拖入事件
    def dragEnterEvent(self, evn):
        # self.setWindowTitle('鼠标拖入窗口了')
        self.lineEdit.setText(evn.mimeData().text()[8:])###'文件路径：\n' +

        self.textEdit.setText('文件路径：\n' + evn.mimeData().text()[8:])
        # 鼠标放开函数事件
        self.path=evn.mimeData().text()[8:]
        print(self.path)
        evn.accept()
    def all_screen(self):##整体截图
        from PIL import ImageGrab
        im = ImageGrab.grab()
        im.save("1.png")
        self.textEdit.setText('截图成功')
        self.path = r'1.png'
    def shuoming(self):
        self.textEdit.setText('截图快捷键：ctrl+alt+a\nocr快捷键：enter\n识别出来的内容会自动复制到剪贴板上\n只能识别图片格式，gif无效')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app = QApplication.instance() or QApplication(sys.argv)
    # app.setStyleSheet(open("设置按钮样式.qss", encoding='utf8').read())
    a = WScreenShot()
    w = MyWindow()##总界面创建
    w.pushButton.clicked.connect(w.read_file)
    #w.pushButton.clicked.connect(w.read_file)
    w.pushButton_2.clicked.connect(w.ocr_fenxi)
    w.pushButton_3.clicked.connect(w.cancel)
    # w.pushButton_4.clicked.connect(w.all_screen)
    w.pushButton_4.clicked.connect(a.run)
    w.setWindowIcon(QtGui.QIcon('favicon.ICO'))
    w.pushButton_5.clicked.connect(w.shuoming)
    w = CandyWindow.createWindow(w,'greenblue','OCR_by_ylh','favicon.ICO')

    #w.setStyleSheet("#MainWindow{border-image:url(bg.jpg);}")
    w.show()

    # w.connect(w.pushButton_2, QtCore.pyqtSignal('clicked()'), w.kaishi)
    # w.pushButton_2.clicked.connect(w.kaishi)
    # w.pushButton_2.clicked.connect(w.progress_bar)
    #w.pushButton_3.clicked.connect(w.cancel)
    sys.exit(app.exec_())
