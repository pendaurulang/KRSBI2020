int timearc = 3000;

void rotatetest() {
  //  motor(1, 250, 240, 250, 225); //kiri
  motor(2, 245, 235, 250, 225);
  delay(timearc);
  motor(0, 0, 0, 0, 0);
  delay(timearc / 6);
  motor(4, 250, 240, 250, 225);
  delay(timearc * 3);
  motor(0, 0, 0, 0, 0);
  delay(timearc / 6);
  motor(1, 250, 240, 250, 225);
  delay(timearc);
}
