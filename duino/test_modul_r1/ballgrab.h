#define ballgrb 51

void ballgrab_init() {
  pinMode(ballgrb, OUTPUT);
}

void grabball() {
  if (valballdtcgrb < ball_thd ) {
    digitalWrite(ballgrb, HIGH);
    //delay(2000);
    //tendang();
  }
  else
    digitalWrite(ballgrb, LOW);
}
