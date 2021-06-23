# modul yang berisi prosedur utama yang dilakukan oleh robot
# import class RobotKRSBIB

import RPi.GPIO as GPIO
from RobotClass import RobotKRSBIB
import FungsiRobot as FungsiRobot

# buat instance robot1 dari class RobotKRSBIB dengan setingan pin default
robot1 = RobotKRSBIB()

while True:
    letak_bola = robot1._cariBola()     # cari letak bola
    while not letak_bola:           # selama letak bola belum ditemukan
        robot1._belokKiri()
        letak_bola = robot1._cariBola()

    robot1._kirimData(None, "bola ditemukan")  # kirim data ke robot 2
    FungsiRobot.kejarBola(robot1, letak_bola)

    jlhOperan = 0
    while jlhOperan < 3:     # ulangi mengoper dan mencari gawang sebanyak 3 kali
        letak_kawan = robot1._cariKawan()   # cari letak kawan
        while not letak_kawan:      # selama kawan belum ditemukan
            robot1._belokKiri()     # belok kiri terus
            letak_kawan = robot1._cariKawan()   # cari kembali kawannya

        FungsiRobot.operKawan(robot1, letak_kawan)  # oper bola ke kawan
        jlhOperan += 1      # tambah jumlah operan yang sudah dilakukan

        letak_gawang = robot1._cariGawang()     # cari letak gawang
        while not letak_gawang:     # selama letak gawang belum ditemukan
            robot1._belokKiri()     # belok kiri terus
            letak_gawang = robot1._cariGawang()     # cari kembali gawangnya

        FungsiRobot.dekatiGawang(letak_gawang)  # dekati gawang

    # bagian ini untuk mencari gawang dan mendekatinya smpe kurang dri 200
    robot1._casKapasitor(20)
    letak_gawang = robot1._cariGawang()     # cari kembali gawang
    while not letak_gawang or letak_gawang > 200:       # selama gawang belum dekat
        if not letak_gawang:
            robot1._belokKiri()
            letak_gawang = robot1._cariGawang()
            continue
        FungsiRobot.dekatiGawang(letak_gawang)  # dekati lagi gawangnya

    robot1._tendangBola()

# jika terjadi error yang tak terduga
while False:
    robot1._belokKanan()

GPIO.cleanup()      # non-aktifkan pin GPIO raspberry pi
robot1.camera.release()    # non-aktifkan kamera