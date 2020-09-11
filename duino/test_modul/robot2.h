void kondisi1r2() {
  kondisi = "kondisi 1 r2";
  if (m1 > 0) {
    motor(5, 200, 200, 200, 200);
  }
  else if (m1 < 0) {
    motor(6, 200, 200, 200, 200);
  }
  else {
    motor(0, 0, 0, 0, 0);
    delay(5000);
  };
}

void kondisi2r2() {
  kondisi = "kondisi 2 r2";
  if (valballdtc < 150 && valballdtc != 0 ) {
    digitalWrite(ballgrb, HIGH);
    delay(5000);
  }
  else
    kondisi1();
}
void kondisi3r2() {
  kondisi = "kondisi 3 r2";
  if (m1 > 0) {
    motor(5, 200, 200, 200, 200);
  }
  else if (m1 < 0) {
    motor(6, 200, 200, 200, 200);
  }
  else {
    delay(2000);
    umpan();
  };
}
