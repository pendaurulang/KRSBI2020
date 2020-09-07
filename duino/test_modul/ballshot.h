int ballsht=50;

void ballshot_init(){
  pinMode(ballsht,OUTPUT);
}
void tendang(){
  digitalWrite(ballsht, HIGH);
  delay(50);
  digitalWrite(ballsht, LOW);
}
