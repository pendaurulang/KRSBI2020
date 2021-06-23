# modul yang berisi fungsi" untuk robot
# import library yang akan digunakan
import numpy as np
from collections import deque
import cv2
import RPi.GPIO as GPIO
from threading import Timer
import serial

class RobotKRSBIB():
    def __init__(self, **pinSettings):
        # settingan default pin robot
        self.pinNumbers = { 'kaki1_RPWM' : 18, 'kaki1_LPWM' : 23,
                            'kaki2_RPWM' : 24, 'kaki2_LPWM' : 25,
                            'kaki3_RPWM' : 17, 'kaki3_LPWM' : 27,
                            'giring1_RPWM' : 1, 'giring1_LPWM' : 2,
                            'giring2_RPWM' : 2, 'giring2_LPWM' : 4,
                            'chargePin' : 5, 'shootPin' : 6 }

        # JIKA KITA INGIN MENGUBAH SETINGAN DEFAULT PIN ROBOT
        if pinSettings:
            # AMBIL KEY DAN VALUE DARI KEYWORD ARGUMENT YANG DIBERIKAN
            # LALU MASUKKAN VALUE TERSEBUT KE KEY YANG TEPAT PADA PINNUMBERS
            for namaPin, nomorPin in pinSettings.items():
                self.pinNumbers[namaPin] = nomorPin

        # SETUP PIN ROBOT
        GPIO.setmode(GPIO.BCM)  # atur penomoran pin dengan mode BCM
        GPIO.setwarnings(False)  # biar ga ada muncul warning jika pin belum di non-aktifkan

        # set semua pin dalam pinNumber sebagai output
        for namaPin, nomorPin in self.pinNumbers.items():
            GPIO.setup( self.pinNumbers[namaPin], GPIO.OUT )

        # matikan seluruh sistem penendang ketika robot dinyalakan
        GPIO.output(self.pinNumbers['chargePin'], 0)
        GPIO.output(self.pinNumbers['shootPin'], 0)

        # set frekuensi pwm motor kaki penggerak
        self.kaki1_RPWM = GPIO.PWM(self.pinNumbers['kaki1_RPWM'], 100)  # set RPWM kaki 1 dengan frekuensi 100 Hz
        self.kaki1_LPWM = GPIO.PWM(self.pinNumbers['kaki1_LPWM'], 100)  # set LPWM kaki 1 dengan frekuensi 100 Hz

        self.kaki2_RPWM = GPIO.PWM(self.pinNumbers['kaki2_RPWM'], 100)  # set RPWM kaki 2 dengan frekuensi 100 Hz
        self.kaki2_LPWM = GPIO.PWM(self.pinNumbers['kaki2_LPWM'], 100)  # set LPWM kaki 2 dengan frekuensi 100 Hz

        self.kaki3_RPWM = GPIO.PWM(self.pinNumbers['kaki3_RPWM'], 100)  # set RPWM kaki 3 dengan frekuensi 100 Hz
        self.kaki3_LPWM = GPIO.PWM(self.pinNumbers['kaki3_LPWM'], 100)  # set LPWM kaki 3 dengan frekuensi 100 Hz

        # set frekuensi pwm motor penggiring
        self.giring1_RPWM = GPIO.PWM(self.pinNumbers['giring1_RPWM'], 100)  # set RPWM penggiring 1 dengan frekuensi 100 Hz
        self.giring1_LPWM = GPIO.PWM(self.pinNumbers['giring1_LPWM'], 100)  # set LPWM penggiring 1 dengan frekuensi 100 Hz

        self.giring2_RPWM = GPIO.PWM(self.pinNumbers['giring2_RPWM'], 100)  # set RPWM penggiring 2 dengan frekuensi 100 Hz
        self.giring2_LPWM = GPIO.PWM(self.pinNumbers['giring2_LPWM'], 100)  # set LPWM penggiring 2 dengan frekuensi 100 Hz

        # buat atribut untuk pin cas dan shoot
        self.chargePin = self.pinNumbers['chargePin']
        self.shootPin = self.pinNumbers['shootPin']
        
        # SETUP KAMERA ROBOT
        # NOTE : ganti nilai (atau bahkan nama) dari orange_low dan orange_high untuk menyesuaiakannya dengan warna bola
        self.orange_low = (0, 176, 25)  # nilai batas bawah warna bola jingga
        self.orange_high = (64, 255, 255)  # nilai batas atas warna bola jingga
        self.BallCenterPoints = deque(maxlen=20)  # struktur data deque untuk menyimpan titik tengah bola yang terekam

        # nilai batas atas dan batas bawah gawang
        self.lower_goal = np.array([0, 0, 225])
        self.upper_goal = np.array([179, 150, 255])

        self.camera = cv2.VideoCapture(0)  # set sumber webcam yang digunakan
        self.camera.set(3, 640)  # set lebar window
        self.camera.set(4, 480)  # set tinggi window
        self.central_x = 320  # set titik tengah window

        # setup komunikasi serial bluetooth
        # NOTE : sebelum menjalankan kode dibawah, pastikan kedua raspberry pi
        #        sudah terhubung dan terdapat file '/dev/rfcomm0'
        self.bluetoothComm = serial.Serial('/dev/rfcomm0')

    # definisi fungsi untuk menggerakkan robot
    def _robotMaju(self):
        self.kaki1_RPWM.ChangeDutyCycle(0)       # kaki 1 searah jarum jam, full power
        self.kaki1_LPWM.ChangeDutyCycle(100)
        self.kaki2_RPWM.ChangeDutyCycle(100)     # kaki 2 berlawanan jarum jam, full power
        self.kaki2_LPWM.ChangeDutyCycle(0)
        self.kaki3_RPWM.ChangeDutyCycle(0)       # kaki 3 stop
        self.kaki3_LPWM.ChangeDutyCycle(0)

        self.giring1_RPWM.ChangeDutyCycle(100)     # penggiring 1 searah jarum jam, full power
        self.giring1_LPWM.ChangeDutyCycle(0)
        self.giring2_RPWM.ChangeDutyCycle(0)   # penggiring 2 berlawanan jarum jam, full power
        self.giring2_LPWM.ChangeDutyCycle(100)

    def _robotMundur(self):
        self.kaki1_RPWM.ChangeDutyCycle(40)      # kaki 1 berlawanan jarum jam, 40% power
        self.kaki1_LPWM.ChangeDutyCycle(0)
        self.kaki2_RPWM.ChangeDutyCycle(0)       # kaki 2 searah jarum jam, 40% power
        self.kaki2_LPWM.ChangeDutyCycle(40)
        self.kaki3_RPWM.ChangeDutyCycle(0)       # kaki 3 stop
        self.kaki3_LPWM.ChangeDutyCycle(0)

        self.giring1_RPWM.ChangeDutyCycle(0)     # penggiring 1 berlawanan jarum jam, 40% power
        self.giring1_LPWM.ChangeDutyCycle(40)
        self.giring2_RPWM.ChangeDutyCycle(40)    # penggiring 2 searah jarum jam, 40% power
        self.giring2_LPWM.ChangeDutyCycle(0)

    def _stopRobot(self):
        self.kaki1_RPWM.ChangeDutyCycle(0)  # kaki 1 stop
        self.kaki1_LPWM.ChangeDutyCycle(0)
        self.kaki2_RPWM.ChangeDutyCycle(0)  # kaki 2 stop
        self.kaki2_LPWM.ChangeDutyCycle(0)
        self.kaki3_RPWM.ChangeDutyCycle(0)  # kaki 3 stop
        self.kaki3_LPWM.ChangeDutyCycle(0)

        self.giring1_RPWM.ChangeDutyCycle(0)  # penggiring 1 stop
        self.giring1_LPWM.ChangeDutyCycle(0)
        self.giring2_RPWM.ChangeDutyCycle(0)  # penggiring 2 stop
        self.giring2_LPWM.ChangeDutyCycle(0)

    def _belokKiri(self):
        self.kaki1_RPWM.ChangeDutyCycle(0)       # kaki 1 berlawanan jarum jam, full power
        self.kaki1_LPWM.ChangeDutyCycle(100)
        self.kaki2_RPWM.ChangeDutyCycle(100)     # kaki 2 searah jarum jam, full power
        self.kaki2_LPWM.ChangeDutyCycle(0)
        self.kaki3_RPWM.ChangeDutyCycle(0)       # kaki 3 berlawanan jarum jam, full power
        self.kaki3_LPWM.ChangeDutyCycle(100)

        self.giring1_RPWM.ChangeDutyCycle(40)    # penggiring 1 searah jarum jam, 40% power
        self.giring1_LPWM.ChangeDutyCycle(0)
        self.giring2_RPWM.ChangeDutyCycle(0)     # penggiring 2 berlawanan jarum jam, 40% power
        self.giring2_LPWM.ChangeDutyCycle(40)

    def _belokKanan(self):
        self.kaki1_RPWM.ChangeDutyCycle(0)       # kaki 1 berlawanan jarum jam, full power
        self.kaki1_LPWM.ChangeDutyCycle(100)
        self.kaki2_RPWM.ChangeDutyCycle(100)     # kaki 2 searah jarum jam, full power
        self.kaki2_LPWM.ChangeDutyCycle(0)
        self.kaki3_RPWM.ChangeDutyCycle(100)     # kaki 3 searah jarum jam, full power
        self.kaki3_LPWM.ChangeDutyCycle(0)

        self.giring1_RPWM.ChangeDutyCycle(40)    # penggiring 1 searah jarum jam, 40% power
        self.giring1_LPWM.ChangeDutyCycle(0)
        self.giring2_RPWM.ChangeDutyCycle(0)     # penggiring 2 berlawanan jarum jam, 40% power
        self.giring2_LPWM.ChangeDutyCycle(40)

    # definisi method untuk mencari bola dan gawang
    def _cariBola(self):
        ret, frame = self.camera.read()      # ambil sebuah frame dari kamera

        blurred = cv2.GaussianBlur(frame, (11, 11), 0)      # blur gambar yang ditangkap kamera
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)      # ubah gambar yang sudah di-blur-kan ke sistem warna HSV

        mask = cv2.inRange(hsv, self.orange_low, self.orange_high)    # buat "mask" untuk warna jingga
        mask = cv2.erode(mask, None, iterations=4)          # lakukan dilasi sebanyak 4 kali
        mask = cv2.dilate(mask, None, iterations=2)         # serta erosi sebanyak 2 kali, untuk menghilangkan noda" kecil

        # cari kontur pada "mask"
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0]
        EnclosingCircleCenter = None

        # apabila terdapat lebih dari 1 kontur pada mask
        if len(contours) > 0:
            # cari kontur terbesar pada "mask" dan gunakan untuk mencari
            # lingkaran yang melingkupinya, serta titik (x, y) lingkaran tersebut
            maxContour = max(contours, key=cv2.contourArea)     # cari kontur terbesar
            ((x, y), radius) = cv2.minEnclosingCircle(maxContour)   # cari lingkaran yang melingkupi kontur teb

            M = cv2.moments(maxContour)
            EnclosingCircleCenter = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))      # titik tengah lingkaran tsb

            '''# jika radius lbh besar dari nol
            if radius > 0:
                # gambarkan lingkaran tersebut dalam frame
                # dan update list titik tengah lingkaran

                # gambar lingkaran di frame, dengan titik tengah (x, y) dan radius = radius, berwarna kuning, dan ketebalan 4
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 4)

                # gambar titik tengah lingkaran tersebut
                # gambar lingkaran di frame, dengan titik tengah (x, y) dan radius = 5, berwarna kuning, dan ketebalan -1
                cv2.circle(frame, EnclosingCircleCenter, 5, (0, 0, 255), -1)
                x_ball = int(x)     # simpan titik x bola
                y_ball = int(y)     # simpan titik y bola'''

        # masukkan titik tengah bola ke dalam deque
        self.BallCenterPoints.appendleft(EnclosingCircleCenter)

        '''# tunggu inputan selama 1 ms
        key = cv2.waitKey(1) & 0xFF

        # munculkan hasil pendeteksian bola ke dalam frame
        cv2.imshow("Frame", frame)
        cv2.imshow("Hasil HSV", mask)

        # print titik tengah bola dan radiusnya
        print("x, y", x_ball, y_ball)
        print("radius bola", radius)

        if x_ball < 200:    # jika bola terlalu kiri
            self._belokKiri()    # suruh robot belok kiri
            print("kiri")   # print "kiri" di terminal
            time.sleep(0.2)  # delay selama 0.2 detik
            self._stopRobot()    # suruh robot berhenti
            print("stop")   # print "stop" di terminal
        elif x_ball > 500:  # jika bola terlalu kanan
            self._belokKanan()   # suruh robot belok kanan
            print("kanan")  # print "kanan" di terminal
            time.sleep(0.2)  # delay selama 0.2 detik
            self._stopRobot()    # suruh robot berhenti
            print("stop")   # print "stop" di terminal
        elif x_ball >= 200 and x_ball <= 500:   # jika bola berada di tengah
            self._robotMaju()    # maju teros
            print("Robot Maju")  # print "Robot Maju" di terminal'''

        # kembalikan data bola yang sudah terdeteksi
        return (x, y, radius)

    def _cariGawang(self):
        ret, frame = self.camera.read()     # ambil sebuah frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # convert frame ke HSV

        mask = cv2.inRange(hsv, self.lower_goal, self.upper_goal)       # buat mask untuk gawang
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel)                      # lakukan proses erosi pada mask
        dilation = cv2.dilate(mask, kernel, iterations=1)   # lakukan proses dilasi pada mask
        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)   # lakukan proses closing pada mask
        closing = cv2.GaussianBlur(closing, (5, 5), 0)      # blurkan mask
        edges = cv2.Canny(closing, 100, 200)                # lakukan deteksi sisi pada mask

        contours = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    # cari kontur pada mask
        contours = contours[0]
        goalCenterPoint = None

        for cnt in contours:
            area = cv2.contourArea(cnt)     # hitung luas kontur
            approx = cv2.approxPolyDP(cnt, 0.001 * cv2.arcLength(cnt, True), True)      # aproksimasi kurva poligonal
            a = approx[0]
            M = cv2.moments(cnt)
            if 1000 < area < 325156:        # jika luasnya lebih dari 1000 dan kurang dari 325156
                if len(contours) > 0:       # jika terdapat lebih dari 1 kontur
                    # cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)      # gambarkan kontur pada window
                    x, y, width, height = cv2.boundingRect(approx)       # cari letak dan ukuran dari persegi panjang yang melingkupi gawang
                    # cv2.rectangle(frame, (x, y), (x + w, y + h), (False), 0)    # gambarkan persegi panjang pada frame
                    # a = cv2.rectangle(frame, (x, y), (x + w, y + h), (False), 0)
                    # cv2.putText(frame, "w={},h={}".format(w, h), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                # (36, 255, 12), 2)     # menampilkan teks pada frame
                    Nilai_x = int(width / 2) + x
                    Nilai_y = int(height / 2) + y
                '''if 1000 < area < 325156:
                    center = (Nilai_x, Nilai_y)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    cv2.putText(frame, "Goal", (center), font, 1, (0, 255, 255))'''

        '''print("High of goal:", h)
        print("Weight of goal", w)
        print("x_goal", Nilai_x)
        print("y_goal", Nilai_y)
        print("Area", area)  # calculate moments for each contour
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("kernel", kernel)'''

        '''if area >= 1000:
            if 287 < h < 320 and 516 < w < 604:
                print("Robot menendang Bola")
            elif h < 287 or w < 516:
                print(" Robot Maju Kedepan")
        else:
            print("Robot menendang")'''

        return (Nilai_x, Nilai_y, width, height)

    def _cariKawan(self):
        # robot diberi tanda kertas warna merah untuk membedakannya dengan objek lainnya
        # sehingga, robot dapat mengenali kawannya
        pass

    # definisi method untuk sistem penendang
    def _casKapasitor(self, waktuCas):
        GPIO.output(self.chargePin, 1)  # nyalakan chargePin sehingga kapasitor akan mengecas
        Timer(waktuCas, GPIO.output, [self.chargePin, 0]).start()   # matikan chargePin setelah beberapa detik telah
                                                                    # berlalu (nilai ini diatur oleh waktuCas

    def _tendangBola(self):
        GPIO.output(self.shootPin, 1)   # nyalakan shootPin sehingga sistem penendang menyala
        Timer(1, GPIO.output, [self.shootPin, 0]).start()   # tunggu hingga 1 detik agar kapasitor benar" kosong
                                                            # lalu matikan sistem penendang

    # definisi method untuk berkomunikasi dengan robot lainnya
    def _kirimData(self, target, data):
        self.bluetoothComm.write(data)

    def _terimaData(self, pengirim):
        data = self.bluetoothComm.readline()
        return data