#define trig 7

int rimut = 0;
char bluetut;

void setup() {
  pinMode(trig, OUTPUT);
  Serial.begin(9600);
  digitalWrite(trig, LOW);
}

void loop() {
 if (Serial.available() > 0) {
    char bluetut = Serial.read();
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
  Serial.println(rimut);
}
