#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 21:12
# @Author  : ylh
# @FileName: ocr_try1.py
# @Software: PyCharm
import pytesseract as p
from PIL import Image
# p.pytesseract.tesseract_cmd='E:/A_Ctf_Tool/Tesseract-OCR/tesseract.exe'
p.pytesseract.tesseract_cmd='E:/A_Ctf_Tool/Tesseract-OCR/tesseract.exe '
text=p.image_to_string(Image.open('C:/Users/asus/Desktop/2.jpg'),lang='chi_sim')
print(text)
# import os
# a = 'tesseract'
# r_file = 'C:/Users/asus/Desktop/1.jpg'
# w_file = 'C:/Users/asus/Desktop/2.txt'
#
# os.system('pip')
