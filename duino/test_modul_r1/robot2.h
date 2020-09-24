void kondisi1r2() {
  kondisi = "kondisi 1 r2";
  kondisi_set = 11;
  if (m1 > 20) {
    motor(5, 200, 200, 200, 200);
  }
  else if (m1 < -20) {
    motor(6, 200, 200, 200, 200);
  }
  else {
    motor(0, 0, 0, 0, 0);
    delay(5000);
  };
}

void kondisi2r2() {
  kondisi = "kondisi 2 r2";
  kondisi_set = 12;
  delay(5000);
  if (valballdtc < 150 && valballdtc != 0 ) {
    delay(5000);
    kondisi_set = 13;
  }
  else {
    kondisi_set = 11;
  };
}
void kondisi3r2() {
  kondisi = "kondisi 3 r2";
  kondisi_set = 13;
  if (m1 > 20) {
    motor(5, 200, 200, 200, 200);
  }
  else if (m1 < -20) {
    motor(6, 200, 200, 200, 200);
  }
  else {
    delay(2000);
    umpan();
    kondisi_set = 11;
  };
}
