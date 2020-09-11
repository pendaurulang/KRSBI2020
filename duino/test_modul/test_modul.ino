int valballdtc;
int valline1;
int valline2;
int rimut = 0;
int t = 0;
int usbread;
char bluetut;
String kondisi = "null";

#define line1 A0
#define line2 A1
#define balldtc A2
#define ballgrb 51

#include "pid.h"
#include "serialparse.h"
#include "ballshot.h"

#include "robot1.h"
#include "robot2.h"
#include "kiper.h"

void setup() {
  ballshot_init();
  serialinit();
  motorinit();
  Serial1.begin(9600);
  pinMode(line1, INPUT);
  pinMode(line2, INPUT);
  pinMode(balldtc, INPUT);
  pinMode(ballgrb, OUTPUT);
  pinMode(ballsht, OUTPUT);
}

void loop() {
  initpid();
  readline();
  bluetooth();
  getimg();
  grabball();
  monitoring();

  if (rimut == 1) {
    remote();
  } else {
    setop();
  };

}
void readline() {
  valline1 = analogRead(line1);
  valline2 = analogRead(line2);
  valballdtc = analogRead(balldtc);
}

void monitoring() {
  Serial.print("Oranye: ");
  Serial.print(m / 20);
  Serial.print("   ");
  Serial.print("Cyan: ");
  Serial.print(m1 / 20);
  Serial.print("   ");
  Serial.print("Magenta: ");
  Serial.print(m2 / 20);
  Serial.print("   ");
  Serial.print("Gawang: ");
  Serial.print(m3 / 20);
  Serial.print("   ");
  Serial.print("Kostum: ");
  Serial.print(m5);
  Serial.print("   ");
  Serial.print("Ball: ");
  Serial.print(valballdtc);
  Serial.print("   ");
  Serial.print("line 1: ");
  Serial.print(valline1);
  Serial.print("   ");
  Serial.print("line 2: ");
  Serial.print(valline2);
  Serial.print("   ");
  Serial.print("Remote: ");
  Serial.print(rimut);
  Serial.print("   ");
  Serial.print("kondisi: ");
  Serial.print(kondisi);
  Serial.println("   ");
}


void remote() {
  kondisi1r2();
}

void bluetooth() {
  if (Serial1.available() > 0) {
    char bluetut = Serial1.read();
    if (bluetut == 'F') {
      rimut = 1;
      if (rimut > 1) {
        rimut = 1;
      };
    }
    else if (bluetut == 'B') {
      rimut = 0;
    }
    else {
      rimut = rimut;
    }
  }
}


void grabball() {
  if (valballdtc < 150 && valballdtc != 0 ) {
    digitalWrite(ballgrb, HIGH);
    //delay(2000);
    //tendang();
  }
  else
    digitalWrite(ballgrb, LOW);
}
