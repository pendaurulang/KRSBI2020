from __future__ import division
import cv2
import numpy as np
import time
import serial
import os
import imutils
import math
import smbus

address = 0x0d
bus = smbus.SMBus(1)

usbcom = serial.Serial('/dev/ttyACM0',9600)

def read_byte(adr): #communicate with compass 
    return bus.read_byte_data(address, adr) 

def read_word(adr): 
    low = bus.read_byte_data(address, adr) 
    high = bus.read_byte_data(address, adr+1) 
    val = (high<< 8) + low 
    return val 

def read_word_2c(adr): 
    val = read_word(adr) 
    if (val>= 0x8000):
        return -((65535 - val)+1) 
    else: 
        return val 

def write_byte(adr,value): 
    bus.write_byte_data(address, adr, value) 

def nothing(*arg):
    pass


FRAME_WIDTH = 320
FRAME_HEIGHT = 240
vidCapture = cv2.VideoCapture(1)
vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)


compas=27
cv2.namedWindow('compas')
cv2.createTrackbar('deg', 'compas', compas, 360, nothing)

while True:
    deg = cv2.getTrackbarPos('deg', 'compas')
    write_byte(11, 0b00000001) 
    write_byte(10, 0b00100000) 
    write_byte(9, 0b00000000|0b00000000|0b00001100|0b00000001) 
    scale = 0.94 
    x_offset = -10 
    y_offset = 10 
    x_out = (read_word_2c(0)) * scale  #calculating x,y,z coordinates 
    y_out = (read_word_2c(2))* scale 
    z_out = read_word_2c(4) * scale
    bearing = math.atan2(y_out, x_out)+.48  #0.48 is correction value 
    if(bearing < 0): 
        bearing += 2* math.pi
    print ("Bearing:", math.degrees(bearing))
    print ("x: ", x_out)
    print ("y: ", y_out)
    print ("z: ", z_out)
    time.sleep(0.1)
    # Get webcam frame
    _, frm = vidCapture.read()
    #frame = imutils.rotate(frm, 180)
    frame = frm
    # Show the original image.
    cv2.imshow('compas', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break



cv2.destroyAllWindows()
vidCapture.release()