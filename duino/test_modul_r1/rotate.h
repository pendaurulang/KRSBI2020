int rot;

void rotate(int dir, int par) {
  int rot = (abs(par) / 160) * 200;
  if (rot > 200) {
    rot = 200;
  }
  motor(dir, rot, rot, rot, rot);
}
