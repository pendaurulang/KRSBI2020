int valballdtc;
int valballdtcgrb;
int valline1;
int valline2;

#define line1 A0
#define line2 A1
#define balldtc A2
#define balldtcgrb A3

void sensor_init() {
  pinMode(line1, INPUT);
  pinMode(line2, INPUT);
  pinMode(balldtc, INPUT);
  pinMode(balldtcgrb, INPUT);
}

void readsensor() {
  valline1 = analogRead(line1);
  valline2 = analogRead(line2);
  valballdtc = analogRead(balldtc);
  valballdtcgrb = analogRead(balldtcgrb);
}
