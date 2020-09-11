void kondisi1() {
  kondisi = "kondisi 1 r1";
  if (valballdtc > 1)
  {
    if (t == 0)
    {
      motor(1, 255, 235, 255, 255);
      delay(5000);
      t = 1;
    }
    else
    {
      test(m, 1);
    }
  } else
  {
    t = 0;
    motor(0, 0, 0, 0, 0);
  }
}

void kondisi2() { 
  kondisi = "kondisi 2 r1";
  if (valballdtc < 150 && valballdtc != 0) {
    if (m1 < 1) {
      motor(6, 255, 255, 255, 255);
      delay(5000);
      tendang();
    }
  }
  else
    kondisi1();//
}
