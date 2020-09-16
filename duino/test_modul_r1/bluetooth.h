#define trig 7

int rimut = 0;
char bluetut;

void bluetooth_init() {
  pinMode(trig, OUTPUT);
  Serial1.begin(9600);
  digitalWrite(trig, LOW);
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
  if (rimut == 1) {
    digitalWrite(trig, HIGH);
  }
  else {
    digitalWrite(trig, LOW);
  }
}
