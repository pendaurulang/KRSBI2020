char a,b,c;
String inp="",inp1="",inp2="",inp3="",inp5="";
int p,p1,p2,p3,p5;
int m,m1,m2,m3,m5;

void serialinit(){
  Serial.begin(9600);
}

void getimg(){
   while(Serial.available())
  {
    a=Serial.read();
    
    if (a=='a')
    {p=inp.toInt(); inp="";}else
    {inp=inp+a;};

    if (a=='b')
    {p1=inp1.toInt(); inp1="";}else
    {inp1=inp1+a;};

    if (a=='c')
    {p2=inp2.toInt(); inp2="";}else
    {inp2=inp2+a;};

    if (a=='d')
    {p3=inp3.toInt(); inp3="";}else
    {inp3=inp3+a;};

    if (a=='f')
    {p5=inp5.toInt(); inp5="";}else
    {inp5=inp5+a;};
  //Serial.println(p);
  }
  //clockwise();
  m=p;
  m1=p1;
  m2=p2;
  m3=p3;
  m5=p5;
  //Serial.println(m);
  
}
