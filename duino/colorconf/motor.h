

void motor(char po, char pwm1, char pwm2, char pwm3, char pwm4) //MOTOR
{
//  if(p==0)//berhenti
//    { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
  if(po==0)//berhenti
 { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
  if(po==1)//maju
    { digitalWrite(in1,LOW); digitalWrite(in2,HIGH); digitalWrite(in3,LOW);  digitalWrite(in4,HIGH);digitalWrite(in5,HIGH); digitalWrite(in6,LOW); digitalWrite(in7,HIGH);  digitalWrite(in8,LOW);};
//  if(p==2)//mundur
//    { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
  if(po==3)//kiri
   { digitalWrite(in1,HIGH); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,HIGH);digitalWrite(in5,LOW); digitalWrite(in6,HIGH); digitalWrite(in7,HIGH);  digitalWrite(in8,LOW);};
  if(po==4)//kanan
    { digitalWrite(in1,LOW); digitalWrite(in2,HIGH); digitalWrite(in3,HIGH);  digitalWrite(in4,LOW);digitalWrite(in5,HIGH); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,HIGH);};
//      
    analogWrite(4,pwm1);
    analogWrite(5,pwm2);
    analogWrite(3,pwm3);
    analogWrite(2,pwm4);
}
