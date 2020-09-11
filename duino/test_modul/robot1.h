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
  if (valballdtc < 150 && valballdtc != 0) {
    if (m1 < 1) {
      motor(6, 255, 255, 255, 255);
    }
    if (m == 0) {
      delay(5000);
      tendang();
      kondisi_set=3;
    }
  }
  else {
    kondisi_set = 1;
  };//
}
