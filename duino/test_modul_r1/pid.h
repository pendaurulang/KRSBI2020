#include "motor.h"

double Sp = 10, pw = 220;
double np = 10, ni = 2, nd = 0, Pv, l_pv, Ts, error = 0, l_error = 0, l_output, output; //nilai variable pada PID
double ys, l;
double ki, ka;

void initpid() {
  ys = ((millis() - l) / 1000);
  l = millis();
}

void test(int obj, int movement)
{

  Pv = ((obj / 20) + 10);
  error = Sp - Pv;
  output = (np * error) + (ni * (error + l_error) * Ts) + ((nd / ys) * (error - l_error));
  l_error = error;
  l_pv = Pv;
  ka = pw + output;
  ki = pw - output;

  if (ki > pw) {
    ki = pw;
  };
  if (ka > pw) {
    ka = pw;
  };
  //if (output < 1 ) {output=1;};
  motor(movement, ki, ka, ki, ka);
  //Serial.print();
}
