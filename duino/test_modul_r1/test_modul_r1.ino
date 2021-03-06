String kondisi = "null";
int kondisi_set = 0;
int line_thd1 = 250; //kalibrasi sensor garis
int linethd_kiri = 250;
int ball_thd1 = 150; //kalibrasi sensor bola (ball grab)
int ball_thd = 400;

#include "sensor.h"
//#include "bluetooth.h"
#include "pid.h"
#include "rotate.h"
#include "serialparse.h"
#include "ballgrab.h"
#include "ballshot.h"
#include "monitor.h"

#include "robot1.h"
#include "robot2.h"
#include "kiper.h"
#include "emergency.h"

void setup() {
  sensor_init();
  ballgrab_init();
  ballshot_init();
  serialinit();
  motorinit();
  kondisi_set = 6;
  //  bluetooth_init();
}

void loop() {
  initpid();
  readsensor();
  //  bluetooth();
  getimg();
  grabball();
  remote();
  monitoring();


  //  if (rimut == 1) {
  //    remote();
  //  } else {
  //    setop();
  //  };

}

void remote() {
  robot1();
}

void robot1() {

  if (kondisi_set == 5) {
    kondisi_set = 5;
    kondisi5();
  }
  if (kondisi_set == 4) {
    kondisi_set = 4;
    kondisi4();
  }
  if (kondisi_set == 3) {
    kondisi_set = 3;
    kondisi3();
  }
  if (kondisi_set == 2) {
    kondisi_set = 2;
    kondisi2();
  }
  if (kondisi_set == 1) {
    kondisi_set = 1;
    kondisi1();
  }
  if (kondisi_set == 6) {
    kondisi_set = 6;
    kondisi_kiri();
  }

}

void robot2() {
  kondisi_set = 11;
  if (kondisi_set == 11) {
    kondisi1r2();
  }
  if (kondisi_set == 12) {
    kondisi2r2();
  }
  if (kondisi_set == 13) {
    kondisi3r2();
  }
}
