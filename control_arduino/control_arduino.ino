/*
 * DEVELOPERS
 * Alfredo Solis shanon.4ever@gmail.com
 * Rafael Ramirez mrsblast@gmail.com
*/

#include <Servo.h>

Servo motor1;
Servo motor2;
Servo motor3;
Servo motor4;

char lectura;          //para escribir en el puerto serial
// valores de los motores
float val1 = 30;
float val2 = 30;
float val3 = 30;
float val4 = 30;


void setup() {
  motor1.attach(4);   
  motor2.attach(5);
  motor3.attach(9);
  motor4.attach(10);
  Serial.begin(9600);
  //config_motors();
}

void loop() {
  if(Serial.available()>0){
    lectura = Serial.read();
    Serial.println(lectura);
    if(lectura == 'v'){
      int value = Serial.parseInt();
      set_motors(value);
    }
    if(lectura == 's'){
      stop_motors();  
    }
    if(lectura == 'c'){
      config_motors();
    }
  }
  Serial.flush();
}

void config_motors() {
  Serial.println("configurando");
  motor1.write(160);                 
  motor2.write(160);
  motor3.write(160);
  motor4.write(160);
  delay(2000);
  motor1.write(30);                 
  motor2.write(30);
  motor3.write(30);
  motor4.write(30);
  delay(5000);    
  Serial.println("configurado");
}

void set_motors(int vel){
  if(vel >= 0 || vel <= 100){
    int value = mapeo(vel); 
    motor1.write(value);
    motor2.write(value);
    motor3.write(value);
    motor4.write(value);
  }
}

int mapeo(int vel){
  return (130/100)*vel+30;
}

void stop_motors(){
  motor1.write(30);
  motor2.write(30);
  motor3.write(30);
  motor4.write(30); 
}



