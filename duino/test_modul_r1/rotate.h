int rot;

void rotate(int dir, int par) {
  int rot = (abs(par) / 160) * 220;
  if (rot > 250) {
    rot = 250;
  }
  motor(dir, rot, rot, rot, rot);
}
