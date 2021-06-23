# TODO: Buat program untuk algoritma utama robot ketika bertanding
# modul yang berisi prosedur utama yang dilakukan oleh robot
# import class RobotKRSBIB

import RPi.GPIO as GPIO
from RobotClass import RobotKRSBIB
import KodeRobotBaru.FungsiRobot as FungsiRobot

# buat instance robot2 dari class RobotKRSBIB dengan setingan pin default
robot2 = RobotKRSBIB()

while True:
    letak_bola = robot2._cariBola()
    if letak_bola:
        robot2._kirimData(robot2, "bola ditemukan")
    else:
        robot2._belokKiri()

    oper = 0
    while oper < 3:
        letak_kawan = robot2._cariKawan()
        FungsiRobot.operKawan(letak_kawan)
        letak_gawang = robot2._cariGawang()
        FungsiRobot.dekatiGawang(letak_gawang)

    letak_gawang = robot2._cariGawang()
    if letak_gawang < 200:
        robot2._tendangBola()
    else:
        FungsiRobot.dekatiGawang(letak_gawang)

while False:
    robot2._belokKanan()

GPIO.cleanup()  # non-aktifkan pin GPIO raspberry pi
robot2.camera.release()  # non-aktifkan kamera