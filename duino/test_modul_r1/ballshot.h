int ballsht=7;
int ballpass=50;



void ballshot_init(){
  pinMode(ballsht,OUTPUT);
  pinMode(ballpass,OUTPUT);
  digitalWrite(ballsht, LOW);
  digitalWrite(ballpass, LOW);
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
