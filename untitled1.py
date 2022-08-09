# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:08:55 2021

@author: Jagdish
"""

import cv2

#TRAINSET = "/usr/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml"
DOWNSCALE = 4

webcam = cv2.VideoCapture(0)
cv2.namedWindow("preview")
#classifier = cv2.CascadeClassifier(TRAINSET)


if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False

while rval:

    # detect faces and draw bounding boxes
    minisize = (frame.shape[1]/DOWNSCALE,frame.shape[0]/DOWNSCALE)
    miniframe = cv2.resize(frame, minisize)
    #faces = classifier.detectMultiScale(miniframe)

    cv2.putText(frame, "Press ESC to close.", (5, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255))
    cv2.imshow("preview", frame)

    # get next frame
    rval, frame = webcam.read()

    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]: # exit on ESC
        break