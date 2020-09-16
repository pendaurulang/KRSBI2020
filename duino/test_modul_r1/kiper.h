void kiper() {
  double z = m / 20;
  if (z == 1 || z == -1 || z > 13 || z < -13) {
    motor(0, 0, 0, 0, 0);
  };
  if (z > 1 && z < 13) {
    motor(3, pw, pw, pw, pw);
  };
  if (z < -1 && z > -13) {
    motor(4, pw, pw, pw, pw);
  };
}
