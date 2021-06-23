from __future__ import division
import cv2
import numpy as np
import time
import os
import imutils

def nothing(*arg):
        pass

FRAME_WIDTH = 320
FRAME_HEIGHT = 240

gcol = (33, 10, 255, 255, 99, 255)
kernel = np.ones((5, 5), np.uint8)

cv2.namedWindow('gawang')
# Lower range colour sliders.
cv2.createTrackbar('lowHue3', 'gawang', gcol[0], 255, nothing)
cv2.createTrackbar('lowSat3', 'gawang', gcol[1], 255, nothing)
cv2.createTrackbar('lowVal3', 'gawang', gcol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue3', 'gawang', gcol[3], 255, nothing)
cv2.createTrackbar('highSat3', 'gawang', gcol[4], 255, nothing)
cv2.createTrackbar('highVal3', 'gawang', gcol[5], 255, nothing)
# Itaration fix
cv2.createTrackbar('erode3', 'gawang', giter[0], 20, nothing)
cv2.createTrackbar('dilate3', 'gawang', giter[1], 20, nothing)

vidCapture = cv2.VideoCapture(2)
vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

while True:
    timeCheck = time.time()

    lowHue3 = cv2.getTrackbarPos('lowHue3', 'gawang')
    lowSat3 = cv2.getTrackbarPos('lowSat3', 'gawang')
    lowVal3 = cv2.getTrackbarPos('lowVal3', 'gawang')
    highHue3 = cv2.getTrackbarPos('highHue3', 'gawang')
    highSat3 = cv2.getTrackbarPos('highSat3', 'gawang')
    highVal3 = cv2.getTrackbarPos('highVal3', 'gawang')
    erode3 = cv2.getTrackbarPos('erode3', 'gawang')
    dilate3 = cv2.getTrackbarPos('dilate3', 'gawang')

    _, frm = vidCapture.read()
    frame = frm
    cv2.imshow('frame', frame)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    colorLow3 = np.array([lowHue3,lowSat3,lowVal3])
    colorHigh3 = np.array([highHue3,highSat3,highVal3])
    mask3 = cv2.inRange(frameHSV, colorLow3, colorHigh3)
    erod3 = cv2.erode(mask3, kernel, iterations=erode3)
    dilation3 = cv2.dilate(erod3, kernel, iterations=dilate3)

    cv2.imshow('gawang', dilation3)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
vidCapture.release()
