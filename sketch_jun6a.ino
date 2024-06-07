#include <AM2302-Sensor.h>

const int tempPin = 2;
const int micPin = A0;
const int micDigPin = 4;
AM2302::AM2302_Sensor am2302{tempPin};

void setup() {
  Serial.begin(9600);
  pinMode(tempPin, INPUT);
  pinMode(micDigPin, INPUT);
  pinMode(micPin, INPUT);

  // am2302 initialize 
  while (!am2302.begin()) {
    Serial.println("Error! Please check sensor connection!");
    delay(1000);
  }
  delay(3000);
}

void loop() {
  auto status = am2302.read();
  Serial.print(am2302.get_Temperature());
  Serial.print(", ");
  Serial.print(am2302.get_Humidity());
  Serial.print(", ");
  Serial.print(digitalRead(micDigPin));
  Serial.print(", ");
  Serial.println(analogRead(micPin));
  delay(500);
}
