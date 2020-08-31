#define en0 4 //dpn ka
#define en1 5
#define en2 3 //blk ka
#define en3 2

#define in1 40 //dpnki
#define in2 41
#define in3 42  //dpnka
#define in4 43
#define in5 30 //blkki
#define in6 31
#define in7 32 //blkka
#define in8 33
#define line1 A0
#define line2 A1
#define balldtc A2
/////////////////////////////////////////////////////////////////////kiper/////
double Sp=10,pw=225;
double np=10,ni=2,nd=0,Pv,l_pv,Ts,error=0,l_error=0,l_output,output; //nilai variable pada PID
double ys,l;
double ki,ka;
//////////////////////////////////////////////////////////////////////////

int ballgrb=51;
int ballsht=50;
int valballdtc;
int valline1;
int valline2;
char a,b,c;
String inp="",inp1="",inp2="",inp3="",inp5="";
int p,p1,p2,p3,p5;
int m,m1,m2,m3,m5;
int usbread;
void setup() {
Serial.begin(9600);
  pinMode(line1,INPUT); 
  pinMode(line2,INPUT); 
  pinMode(balldtc,INPUT);
  pinMode(ballgrb,OUTPUT); 
  pinMode(ballsht,OUTPUT);  
  //pwm
  pinMode(en0, OUTPUT);
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);
  pinMode(en3, OUTPUT);
  //logic
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);
  pinMode(in7, OUTPUT);
  pinMode(in8, OUTPUT);



}

void loop() {
ys=((millis()-l)/1000); 
l=millis();
//jalan();
getimg();
grabball();
if (m5 == 0){ //jika cyan
if(((m1/20)<=((m/20)+1)) && ((m1/20)>=((m/20)-1))){
  kiper();
  Serial.println("mandek");
  }else{
test();
Serial.println("golek");};
} else
{
  if(((m2/20)<=((m/20)+1)) && ((m2/20)>=((m/20)-1))){
  kiper();
  Serial.println("mandek");
  }else{
test();
Serial.println("golek");};
}
Serial.print(m/20);
Serial.print("   ");
Serial.print(m1/20);
Serial.print("   ");
Serial.print(m2/20);
Serial.print("   ");
Serial.print(m3/20);
Serial.print("   ");
Serial.print(m5);
Serial.println("   ");
//Serial.print(valline1);
//Serial.print("   ");
//Serial.print(valline2);
//Serial.print("   ");
//
//Serial.print(ki);
//Serial.print("   ");
//Serial.print(ka);
//Serial.print("   ");
//
//Serial.print(output);
//Serial.print("   ");
//
//Serial.println(valballdtc);
//analogWrite(en0, 245);//kadep
//analogWrite(en1, 255);//kidep
//analogWrite(en2, 255);//kibel
//analogWrite(en3, 238);//kabel
}


void stopit() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, LOW);
  digitalWrite(in6, LOW);
  digitalWrite(in7, LOW);
  digitalWrite(in8, LOW);
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
void jalan(){
  if (((m < 150 )&&(m >= 0))||((m > -150 )&&(m <= 0))){
  maju();}
  else if ((m > 150 )&&(m <= 320)){
  clockwise();}//kiri();}
  else if ((m < -150 )&&(m >= -320)){
  aclockwise();}//kanan();}
  else
  stopit();
  }

void grabball(){
valballdtc = analogRead(balldtc);
  //Serial.println(valballdtc);
  if (valballdtc < 100){
    digitalWrite(ballgrb, HIGH);
    }
    else
  digitalWrite(ballgrb, LOW);
}





void motor(char p, char pwm1, char pwm2, char pwm3, char pwm4) //MOTOR
{
//  if(p==0)//berhenti
//    { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
  if(p==0)//berhenti
 { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
  if(p==1)//maju
    { digitalWrite(in1,LOW); digitalWrite(in2,HIGH); digitalWrite(in3,LOW);  digitalWrite(in4,HIGH);digitalWrite(in5,HIGH); digitalWrite(in6,LOW); digitalWrite(in7,HIGH);  digitalWrite(in8,LOW);};
//  if(p==2)//mundur
//    { digitalWrite(in1,LOW); digitalWrite(in2,LOW); digitalWrite(in3,LOW);  digitalWrite(in4,LOW);digitalWrite(in5,LOW); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,LOW);};
  if(p==3)//kiri
   //{ digitalWrite(in1,HIGH); digitalWrite(in2,LOW); digitalWrite(in3,HIGH);  digitalWrite(in4,LOW);};
   //{ digitalWrite(in1,LOW); digitalWrite(in2,HIGH); digitalWrite(in3,LOW);  digitalWrite(in4,HIGH);};
   //{ digitalWrite(in5,HIGH); digitalWrite(in6,LOW); digitalWrite(in7,HIGH);  digitalWrite(in8,LOW);};
   { digitalWrite(in5,LOW); digitalWrite(in6,HIGH); digitalWrite(in7,LOW);  digitalWrite(in8,HIGH);};
     if(p==4)//kanan
    { digitalWrite(in1,LOW); digitalWrite(in2,HIGH); digitalWrite(in3,HIGH);  digitalWrite(in4,LOW);digitalWrite(in5,HIGH); digitalWrite(in6,LOW); digitalWrite(in7,LOW);  digitalWrite(in8,HIGH);};
//      
    analogWrite(4,pwm1);
    analogWrite(5,pwm2);
    analogWrite(3,pwm3);
    analogWrite(2,pwm4);
}
void test()
{
 
    Pv=((m/20)+10);
    error=Sp-Pv;
    output=(np*error)+(ni*(error+l_error)*Ts)+((nd/ys)*(error-l_error));
    l_error=error;
    l_pv=Pv;
    ka=pw+output;
    ki=pw-output;

    if (ki >pw) {ki=pw;};
    if (ka >pw) {ka=pw;};
    //if (output < 1 ) {output=1;};
    motor(1,ki,ka,ki,ka); 
    //Serial.print();   
}

void kiper(){
double z=m/20;
if(z==1 || z==-1 || z>13 || z<-13) {motor(0,0,0,0,0);};
if(z>1 && z<13) {motor(3,pw,pw,pw,pw);};
if(z<-1 && z>-13) {motor(4,pw,pw,pw,pw);};
}
