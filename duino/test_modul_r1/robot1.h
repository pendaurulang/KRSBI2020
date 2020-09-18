void kondisi1() {
  kondisi = "kondisi 1 r1";
  kondisi_set = 1;

  if (valballdtc < 150 && valballdtc != 0) {
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
  if (valballdtc < 150) {
    if (m1 < 0) {
      motor(6, 255, 255, 255, 255);
    }
    else if (m1 > 0) {
      motor(5, 255, 255, 255, 255);
    }
    else {
      motor(0, 0, 0, 0, 0);
      delay(5000);
      umpan();
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

  if (valline1 > line_thd1) {
    if (m3 > 0) {
      motor (5, 255, 255, 255, 255);
    }
    else if (m3 < 0) {
      motor(6, 255, 255, 255, 255);
    }
    else
    {
      motor(1, 255, 255, 255, 255);
    }
  }
  else
  {
    motor(0, 0, 0, 0, 0);
    delay(1000);
    kondisi_set = 4;
  }
}


void kondisi5() {
  kondisi = "kondisi 5 r1";
  kondisi_set = 5;
  if (valballdtc < 150) {
    if (m3 < 0) {
      motor(6, 255, 255, 255, 255);
    }
    else if (m3 > 0) {
      motor(5, 255, 255, 255, 255);
    }
    else {
      motor(0, 0, 0, 0, 0);
      delay(5000);
      tendang();
      kondisi_set = 1;
    }
  }
  else {
    kondisi_set = 4;
  };//
}
