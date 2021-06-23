from __future__ import division
import cv2
import numpy as np
import time
import serial
import os
import imutils
import RPi.GPIO as GPIO
import I2C_LCD_driver
lcd = I2C_LCD_driver.lcd()
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
usbcom = serial.Serial('/dev/ttyACM1',9600)

def nothing(*arg):
        pass

FRAME_WIDTH = 320
FRAME_HEIGHT = 240

# Initial HSV GUI slider values to load on program start.
#icol = (0, 0, 0, 255, 255, 255)
#icol = (36, 202, 59, 71, 255, 255)    # Green
#icol = (18, 0, 196, 36, 255, 255)  # Yellow
#icol = (89, 0, 0, 125, 255, 255)  # Blue
#icol = (0, 100, 80, 10, 255, 255)   # Red
#icol = (0, 88, 146, 78, 255, 255)   1 test
ocol = (0,47, 255, 28, 255, 255)   # New start
ccol = (80, 255, 255, 170, 255, 255)
mcol = (132, 50, 133, 168, 110, 255)
gcol = (36, 0, 191, 129, 141, 255)
oiter = (0,1)
citer = (1,0)
miter = (0,1)
giter = (1,1)

kernel = np.ones((5, 5), np.uint8)

cv2.namedWindow('orange')
# Lower range colour sliders.
cv2.createTrackbar('lowHue', 'orange', ocol[0], 255, nothing)
cv2.createTrackbar('lowSat', 'orange', ocol[1], 255, nothing)
cv2.createTrackbar('lowVal', 'orange', ocol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue', 'orange', ocol[3], 255, nothing)
cv2.createTrackbar('highSat', 'orange', ocol[4], 255, nothing)
cv2.createTrackbar('highVal', 'orange', ocol[5], 255, nothing)

cv2.createTrackbar('erode', 'orange', oiter[0], 20, nothing)
cv2.createTrackbar('dilate', 'orange', oiter[1], 20, nothing)

cv2.namedWindow('cyan')
# Lower range colour sliders.
cv2.createTrackbar('lowHue1', 'cyan', ccol[0], 255, nothing)
cv2.createTrackbar('lowSat1', 'cyan', ccol[1], 255, nothing)
cv2.createTrackbar('lowVal1', 'cyan', ccol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue1', 'cyan', ccol[3], 255, nothing)
cv2.createTrackbar('highSat1', 'cyan', ccol[4], 255, nothing)
cv2.createTrackbar('highVal1', 'cyan', ccol[5], 255, nothing)

cv2.createTrackbar('erode1', 'cyan', citer[0], 20, nothing)
cv2.createTrackbar('dilate1', 'cyan', citer[1], 20, nothing)

cv2.namedWindow('magenta')
# Lower range colour sliders.
cv2.createTrackbar('lowHue2', 'magenta', mcol[0], 255, nothing)
cv2.createTrackbar('lowSat2', 'magenta', mcol[1], 255, nothing)
cv2.createTrackbar('lowVal2', 'magenta', mcol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue2', 'magenta', mcol[3], 255, nothing)
cv2.createTrackbar('highSat2', 'magenta', mcol[4], 255, nothing)
cv2.createTrackbar('highVal2', 'magenta', mcol[5], 255, nothing)

cv2.createTrackbar('erode2', 'magenta', miter[0], 20, nothing)
cv2.createTrackbar('dilate2', 'magenta', miter[1], 20, nothing)

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


# Initialize webcam. Webcam 0 or webcam 1 or ...
vidCapture = cv2.VideoCapture(0)
vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)

while True:
    if GPIO.input(13) == GPIO.HIGH:
        ch = 1
    else:
        ch = 0
    timeCheck = time.time()
    # Get HSV values from the GUI sliders.
    lowHue = cv2.getTrackbarPos('lowHue', 'orange')
    lowSat = cv2.getTrackbarPos('lowSat', 'orange')
    lowVal = cv2.getTrackbarPos('lowVal', 'orange')
    highHue = cv2.getTrackbarPos('highHue', 'orange')
    highSat = cv2.getTrackbarPos('highSat', 'orange')
    highVal = cv2.getTrackbarPos('highVal', 'orange')
    erode = cv2.getTrackbarPos('erode', 'orange')
    dilate = cv2.getTrackbarPos('dilate', 'orange')
#######
    lowHue1 = cv2.getTrackbarPos('lowHue1', 'cyan')
    lowSat1 = cv2.getTrackbarPos('lowSat1', 'cyan')
    lowVal1 = cv2.getTrackbarPos('lowVal1', 'cyan')
    highHue1 = cv2.getTrackbarPos('highHue1', 'cyan')
    highSat1 = cv2.getTrackbarPos('highSat1', 'cyan')
    highVal1 = cv2.getTrackbarPos('highVal1', 'cyan')
    erode1 = cv2.getTrackbarPos('erode1', 'cyan')
    dilate1 = cv2.getTrackbarPos('dilate1', 'cyan')
#######
    lowHue2 = cv2.getTrackbarPos('lowHue2', 'magenta')
    lowSat2 = cv2.getTrackbarPos('lowSat2', 'magenta')
    lowVal2 = cv2.getTrackbarPos('lowVal2', 'magenta')
    highHue2 = cv2.getTrackbarPos('highHue2', 'magenta')
    highSat2 = cv2.getTrackbarPos('highSat2', 'magenta')
    highVal2 = cv2.getTrackbarPos('highVal2', 'magenta')
    erode2 = cv2.getTrackbarPos('erode2', 'magenta')
    dilate2 = cv2.getTrackbarPos('dilate2', 'magenta')
#######
    lowHue3 = cv2.getTrackbarPos('lowHue3', 'gawang')
    lowSat3 = cv2.getTrackbarPos('lowSat3', 'gawang')
    lowVal3 = cv2.getTrackbarPos('lowVal3', 'gawang')
    highHue3 = cv2.getTrackbarPos('highHue3', 'gawang')
    highSat3 = cv2.getTrackbarPos('highSat3', 'gawang')
    highVal3 = cv2.getTrackbarPos('highVal3', 'gawang')
    erode3 = cv2.getTrackbarPos('erode3', 'gawang')
    dilate3 = cv2.getTrackbarPos('dilate3', 'gawang')

    # Get webcam frame
    _, frm = vidCapture.read()
    frame = frm
    # Show the original image.
    cv2.imshow('frame', frame)
    #cv2.imshow('frame',imutils.rotate(frame, 180))

    # Convert the frame to HSV colour model.

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # HSV values to define a colour range we want to create a mask from.
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    erod = cv2.erode(mask, kernel,iterations=erode)
    dilation = cv2.dilate(erod, kernel, iterations=dilate)
    # Show the first mask
    cv2.imshow('orange', dilation)
#######
    colorLow1 = np.array([lowHue1,lowSat1,lowVal1])
    colorHigh1 = np.array([highHue1,highSat1,highVal1])
    mask1 = cv2.inRange(frameHSV, colorLow1, colorHigh1)
    erod1 = cv2.erode(mask1, kernel,iterations=erode1)
    dilation1 = cv2.dilate(erod1, kernel, iterations=dilate1)
    # Show the first mask
    cv2.imshow('cyan', dilation1)
#######
    colorLow2 = np.array([lowHue2,lowSat2,lowVal2])
    colorHigh2 = np.array([highHue2,highSat2,highVal2])
    mask2 = cv2.inRange(frameHSV, colorLow2, colorHigh2)
    erod2 = cv2.erode(mask2, kernel,iterations=erode2)
    dilation2 = cv2.dilate(erod2, kernel, iterations=dilate2)
    # Show the first mask
    cv2.imshow('magenta', dilation2)
#######
    colorLow3 = np.array([lowHue3,lowSat3,lowVal3])
    colorHigh3 = np.array([highHue3,highSat3,highVal3])
    mask3 = cv2.inRange(frameHSV, colorLow3, colorHigh3)
    erod3 = cv2.erode(mask3, kernel,iterations=erode3)
    dilation3 = cv2.dilate(erod3, kernel, iterations=dilate3)
    closing3 = cv2.morphologyEx(dilation3, cv2.MORPH_CLOSE, kernel)   # lakukan proses closing pada mask
    closing3 = cv2.GaussianBlur(closing3, (5, 5), 0)      # blurkan mask
    # Show the first mask
    cv2.imshow('gawang', closing3)


#######data
    im, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im1, contours1, hierarchy1 = cv2.findContours(dilation1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im2, contours2, hierarchy2 = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours3 = cv2.findContours(closing3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours3 = contours3[0]

    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    contour_sizes1 = [(cv2.contourArea(contour1), contour1) for contour1 in contours1]
    contour_sizes2 = [(cv2.contourArea(contour2), contour2) for contour2 in contours2]
    # contour_sizes3 = [(cv2.contourArea(contour3), contour3) for contour3 in contours3]
    
    try:
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        x,y,w,h = cv2.boundingRect(biggest_contour)
    except ValueError:
        biggest_contour = {}
        x=9000
        y=w=h=0
    try:
        biggest_contour1 = max(contour_sizes1, key=lambda x: x[0])[1]
        x1,y1,w1,h1 = cv2.boundingRect(biggest_contour1)
    except ValueError:
        biggest_contour1 = {}
        x1=9000
        y1=w1=h1=0
    try:
        biggest_contour2 = max(contour_sizes2, key=lambda x: x[0])[1]
        x2,y2,w2,h2 = cv2.boundingRect(biggest_contour2)
    except ValueError:
        biggest_contour2 = {}
        x2=9000
        y2=w2=h2=0

    try:
        x3=9000
        y3=w3=h3=0
        for cnt in contours3:
            area = cv2.contourArea(cnt)     # hitung luas kontur
            approx = cv2.approxPolyDP(cnt, 0.001 * cv2.arcLength(cnt, True), True)      # aproksimasi kurva poligonal
            a = approx[0]
            M = cv2.moments(cnt)
            if 1000 < area < 325156:        # jika luasnya lebih dari 1000 dan kurang dari 325156
                if len(contours3) > 0:       # jika terdapat lebih dari 1 kontur
                    # cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)      # gambarkan kontur pada window
                    x3, y3, w3, h3 = cv2.boundingRect(approx)       # cari letak dan ukuran dari persegi panjang yang melingkupi gawang
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (False), 0)    # gambarkan persegi panjang pada frame
                    # a = cv2.rectangle(frame, (x, y), (x + w, y + h), (False), 0)
                    cv2.putText(frame, "w={},h={}".format(w, h), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                (36, 255, 12), 2)     # menampilkan teks pada frame
                    Nilai_x = int(w3 / 2) + x3
                    Nilai_y = int(h3 / 2) + y3
                if 1000 < area < 325156:
                    center = (Nilai_x, Nilai_y)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    cv2.putText(frame, "Goal", (center), font, 1, (0, 255, 255))

    except ValueError:
        biggest_contour3 = {}
        x3=9000
        y3=w3=h3=0

    try:
        o=x-(320-(x+w))
    except NameError:
        o=1000
    try:
        c=x1-(320-(x1+w1))
    except NameError:
        c=1000
    try:
        m=x2-(320-(x2+w2))
    except NameError:
        m=1000
    try:
        gawang=x3-(320-(x3+w3))
    except NameError:
        gawang=1000 

    #usbcom.open()
    usbcom.write(str('a').encode("utf-8"))
    usbcom.write(str(o).encode("utf-8"))
    usbcom.write(str('b').encode("utf-8"))
    usbcom.write(str(c).encode("utf-8"))
    usbcom.write(str('c').encode("utf-8"))
    usbcom.write(str(m).encode("utf-8"))
    usbcom.write(str('d').encode("utf-8"))
    usbcom.write(str(gawang).encode("utf-8"))
    usbcom.write(str('f').encode("utf-8"))
    usbcom.write(str(ch).encode("utf-8"))

# data reading

    # read_serial=usbcom.readline()
    # serial_data = str(read_serial,'cp1252')
    # data = serial_data.split('_')
    # kondisi = data[10]
    # usbcom.close()



    if ch == 0:
        wrn = "cyan"
    else:
        wrn = "magenta"
    lcd.lcd_clear()
    lcd.lcd_display_string(str(wrn),1)
    # lcd.lcd_display_string(str(kondisi),1)
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    print('fps - ', 1/(time.time() - timeCheck))
    print('Orange: ',o,'  ','Cyan: ',c,'  ','Magenta: ',m,'  ','Gawang: ',gawang,'  ','Kostum: ',wrn)
    # print('Orange: ',o,'  ','Cyan: ',c,'  ','Magenta: ',m,'  ','Gawang: ',gawang,'  ','Kostum: ',wrn,'  ','grab1: ',data[6],'  ','grab2: ',data[7],'  ','line1: ',data[8],'  ','line2: ',data[9],'  ','kondisi: ',data[10],'  ','Kode: ',data[11])

cv2.destroyAllWindows()
vidCapture.release()
