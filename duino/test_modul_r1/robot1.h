void kondisi1() {
  kondisi = "kondisi 1 r1";
  kondisi_set = 1;

  if (valballdtcgrb < ball_thd1) {
    motor(0, 0, 0, 0, 0);
    kondisi_set = 2;
  }
  else {
    kondisi_set = 1;
    test(m, 1);
  };


}

void kondisi2() {
  kondisi = "kondisi 2 r1";
  kondisi_set = 2;
  if (valballdtcgrb < ball_thd1) {
    if (m1 < -20) {
      rotate(6, m1);
    }
    else if (m1 > 20) {
      rotate(5, m1);
    }
    else {
      motor(0, 0, 0, 0, 0);
      delay(1000);
      tendang();
      kondisi_set = 3;
    }
  }
  else {
    kondisi_set = 1;
  };//
}

void kondisi3() {
  kondisi = "kondisi 3 r1";
  kondisi_set = 3;
  if (m3 < -20) {
    rotate(6, m3);
  }
  else if (m3 > 20) {
    rotate(5, m3);
  }
  else {
    if (valline1 > line_thd1) {
      motor(1, 220, 220, 220, 220);
    }
    else {
      motor(0, 0, 0, 0, 0);
      kondisi_set = 4;
    }

  }
}

//void kondisi3() {
//  kondisi = "kondisi 3 r1";
//  kondisi_set = 3;
//
//  if (valline1 > line_thd1) {
//    //    if (m3 > 20) {
//    //      rotate(5, m3);
//    //    }
//    //    else if (m3 < -20) {
//    //      rotate(6, m3);
//    //    }
//    //    else
//    //    {
//    //      motor(1, 255, 255, 255, 255);
//    //    }
//    test(m3, 1);
//  }
//  else
//  {
//    motor(0, 0, 0, 0, 0);
//    //    delay(1000);
//    kondisi_set = 4;
//  }
//}

void kondisi4() {
  kondisi = "kondisi 4 r1";
  kondisi_set = 4;
  if (valballdtcgrb > ball_thd1) {
    if (m1 < -50 ) {
      rotate(6, m1);
    }
    else if (m1 > 50) {
      rotate(5, m1);
    }
    else {
      motor(0, 0, 0, 0, 0);
    }

  }
  else {
    motor(0, 0, 0, 0, 0);
    kondisi_set = 5;
  }

}

void kondisi5() {
  kondisi = "kondisi 5 r1";
  kondisi_set = 5;
  if (valballdtcgrb < ball_thd1) {
    if (m3 < -50) {
      rotate(6, m3);
      kondisi_set = 5;
    }
    else if (m3 > 50) {
      rotate(5, m3);
      kondisi_set = 5;
    }
    else {
      motor(0, 0, 0, 0, 0);
      delay(1000);
      tendang();
      kondisi_set = 1;
    }
  }
  else {
    kondisi_set = 4;
  }//
}

void kondisi_kiri() {
  kondisi = "kondisi kiri";
  kondisi_set = 6;
  if (valline1 < linethd_kiri) {
    motor(0, 0, 0, 0, 0);
    kondisi_set = 1;
  }
  else
  {
    motor(3, 230, 230, 230, 230);
  }
}
