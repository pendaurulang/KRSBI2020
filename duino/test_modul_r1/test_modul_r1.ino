String kondisi = "null";
int kondisi_set = 0;

#include "sensor.h"
//#include "bluetooth.h"
#include "pid.h"
#include "serialparse.h"
#include "ballgrab.h"
#include "ballshot.h"
#include "monitor.h"

#include "robot1.h"
#include "robot2.h"
#include "kiper.h"

void setup() {
  sensor_init();
  ballgrab_init();
  ballshot_init();
  serialinit();
  motorinit();
//  bluetooth_init();
}

void loop() {
  initpid();
  readsensor();
//  bluetooth();
  getimg();
  grabball();
  monitoring();
  remote();

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
  kondisi_set = 1;
  if (kondisi_set = 1) {
    kondisi1();
  }
  if (kondisi_set = 2) {
    kondisi2();
  }
  if (kondisi_set = 3) {
//    kondisi3();
  }
  if (kondisi_set = 4) {
//    kondisi4();
  }
  if (kondisi_set = 5) {
//    kondisi5();
  }
  if (kondisi_set = 6) {
//    kondisi6();
  }
}

void robot2() {
  kondisi_set = 11;
  if (kondisi_set = 11) {
    kondisi1r2();
  }
  if (kondisi_set = 12) {
    kondisi2r2();
  }
  if (kondisi_set = 13) {
    kondisi3r2();
  }
}
