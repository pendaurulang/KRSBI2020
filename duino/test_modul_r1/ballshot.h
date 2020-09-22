int ballsht = 7;
int ballpass = 50;

void ballshot_init() {
  pinMode(ballsht, OUTPUT);
  pinMode(ballpass, OUTPUT);
  digitalWrite(ballsht, LOW);
  digitalWrite(ballpass, LOW);
}
void tendang() {
  digitalWrite(ballsht, LOW);
  delay(50);
  digitalWrite(ballsht, HIGH);
}

void umpan() {
  digitalWrite(ballpass, LOW);
  delay(50);
  digitalWrite(ballpass, HIGH);
}
