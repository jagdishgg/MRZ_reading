from passporteye import read_mrz
import pytesseract
from cv2 import cv2
import numpy as np

image_file='E:\idn\image.jpg'

def process_mrz(mrz1):
    if mrz1.find('784')>0 and mrz1.find('784')<13:
        st1=mrz1.find('784')
        return mrz1[st1:st1+18]
    elif mrz1.find('84')>0 and mrz1.find('84')<13:
        st1=mrz1.find('84')
        return '7'+mrz1[st1:st1+18]
    elif mrz1.find('4')>0 and mrz1.find('4')<12:
        st1=mrz1.find('4')
        return '78'+mrz1[st1:st1+18]
		
from passporteye.mrz.image import MRZPipeline
p = MRZPipeline(image_file)
mrz1=p.data['text'].replace(' ','').replace('-','').split('\n')[0]
mrz_final=process_mrz(mrz1)
print(mrz_final)
