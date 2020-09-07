#include "motor.h"
#include "pid.h"
#include "serialparse.h"
#include "ballshot.h"

#define line1 A0
#define line2 A1
#define balldtc A2
int ballgrb=51;
int valballdtc;
int valline1;
int valline2;
int rimut = 0;
int t = 0;
int usbread;
char bluetut;


void setup() {
  ballshot_init();
  serialinit();
  motorinit();
  Serial1.begin(9600);
  pinMode(line1,INPUT); 
  pinMode(line2,INPUT); 
  pinMode(balldtc,INPUT);
  pinMode(ballgrb,OUTPUT); 
  pinMode(ballsht,OUTPUT);  
}

void loop() {
initpid();
bluetooth();
getimg();
grabball();
monitoring();

if (rimut==1){remote();}else{setop();};

}
void monitoring(){
Serial.print("Oranye: ");
Serial.print(m/20);
Serial.print("   ");
Serial.print("Cyan: ");
Serial.print(m1/20);
Serial.print("   ");
Serial.print("Magenta: ");
Serial.print(m2/20);
Serial.print("   ");
Serial.print("Gawang: ");
Serial.print(m3/20);
Serial.print("   ");
Serial.print("Kostum: ");
Serial.print(m5);
Serial.print("   ");
Serial.print("Ball: ");
Serial.print(valballdtc);
Serial.print("   ");
Serial.print("Remote: ");
Serial.print(rimut);
Serial.println("   ");
}


void remote(){
  kondisi1();
}

void kondisi1(){
  if (valballdtc>1)
  {
    if (t==0)
    {
    motor(1,255,235,255,255);
    delay(5000);
    t=1;
    }
    else 
    {
    test(m,1);
    }
  }else
    {
    t=0;
    motor(0,0,0,0,0);
    }
}

void bluetooth(){
  if (Serial1.available()>0){
    char bluetut= Serial1.read();
    if (bluetut == 'F'){
      rimut=1;
      if (rimut>1){
        rimut=1;
      };
    }
    else if (bluetut == 'B'){
      rimut=0;
    } 
    else{
      rimut=rimut;
    }
  }
}


void grabball(){
valballdtc = analogRead(balldtc);
  //Serial.println(valballdtc);
  if (valballdtc < 150 && valballdtc != 0 ){
    digitalWrite(ballgrb, HIGH);
    delay(2000);
    tendang();
    }
    else
  digitalWrite(ballgrb, LOW);
}

void kiper(){
double z=m/20;
if(z==1 || z==-1 || z>13 || z<-13) {motor(0,0,0,0,0);};
if(z>1 && z<13) {motor(3,pw,pw,pw,pw);};
if(z<-1 && z>-13) {motor(4,pw,pw,pw,pw);};
}

void setop(){
  { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
}
