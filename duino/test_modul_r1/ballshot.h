int ballsht=50;
int ballpass=7;

void ballshot_init(){
  pinMode(ballsht,OUTPUT);
  pinMode(ballpass,OUTPUT);
}
void tendang(){
  digitalWrite(ballsht, HIGH);
  delay(50);
  digitalWrite(ballsht, LOW);
}

void umpan(){
  digitalWrite(ballpass, HIGH);
  delay(50);
  digitalWrite(ballpass, LOW);
}
