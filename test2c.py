import time
import serial
import os
usbcom = serial.Serial('/dev/ttyACM0',9600)

while True:
	
	usbcom.write(str('#').encode("utf-8"))
	usbcom.write(str(22).encode("utf-8"))
	usbcom.write(str('$').encode("utf-8"))
	usbcom.write(str('12').encode("utf-8"))
	usbcom.write(str('@').encode("utf-8"))
	usbcom.write(str(55).encode("utf-8"))
	read_serial=usbcom.readline()
	serial_data = str(read_serial,'cp1252')
	data = serial_data.split('_')
	data1 = data[4]
	print(data1)
