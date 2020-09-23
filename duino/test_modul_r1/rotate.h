int rot;

void rotate(int dir, int par) {
  int rot = (abs(par) / 160) * 255;
  if (rot > 255) {
    rot = 255;
  }
  motor(dir, rot, rot, rot, rot);
}
