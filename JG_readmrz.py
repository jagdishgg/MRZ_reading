# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:28:25 2021

@author: Jagdish
"""

from passporteye import read_mrz
#import pytesseract
#from cv2 import cv2
#import numpy as np
curr_dir="E:\\idn\\"
image_name='6.jpg'
image_file=curr_dir+image_name

def process_mrz(mrz1):
    if mrz1.find('784')>0 and mrz1.find('784')<18:
        st1=mrz1.find('784')
        return mrz1[st1:st1+18]
    elif mrz1.find('84')>0 and mrz1.find('84')<18:
        st1=mrz1.find('84')
        return '7'+mrz1[st1:st1+18]
    elif mrz1.find('4')>0 and mrz1.find('4')<18:
        st1=mrz1.find('4')
        return '78'+mrz1[st1:st1+18]
		
from passporteye.mrz.image import MRZPipeline
p = MRZPipeline(image_file)
p.result
mrz1=p.data['text'].replace(' ','').replace('-','').split('\n')[0]
mrz_final=process_mrz(mrz1)
print(mrz_final)
text_file = open(curr_dir+"final_mrz.txt", "w")
n = text_file.write(mrz_final)
text_file.close()
