int rimut = 0;
char bluetut;

void bluetooth_init() {
  Serial1.begin(9600);
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
