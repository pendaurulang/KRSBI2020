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
                if 1000 < area < 325156:
                    center = (Nilai_x, Nilai_y)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    cv2.putText(frame, "Goal", (center), font, 1, (0, 255, 255))

        print("High of goal:", h)
        print("Weight of goal", w)
        print("x_goal", Nilai_x)
        print("y_goal", Nilai_y)
        print("Area", area)  # calculate moments for each contour
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("kernel", kernel)

        if area >= 1000:
            if 287 < h < 320 and 516 < w < 604:
                print("Robot menendang Bola")
            elif h < 287 or w < 516:
                print(" Robot Maju Kedepan")
        else:
            print("Robot menendang")

        return (Nilai_x, Nilai_y, width, height)