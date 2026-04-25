#include <Servo.h>

const int trigPin = 9;
const int echoPin = 10;
const int LeftEye = 6;
const int RightEye = 7;

Servo servoHead;
Servo servoLeftArm;
Servo servoRightArm;

float lastDistance = 0;
unsigned long lastTime = 0;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(LeftEye, OUTPUT);
  pinMode(RightEye, OUTPUT);

  servoHead.attach(3);
  servoLeftArm.attach(4);
  servoRightArm.attach(5);

  neutralPosition();
}

void loop() {
  float distance = measureDistance();
  unsigned long now = millis();

  if (now - lastTime > 200) {
    float deltaT = (now - lastTime) / 1000.0;
    float speed = (lastDistance - distance) / deltaT; // cm/s(!!!)

    if (speed > 0) {
      Serial.println(speed); 
    }

    lastDistance = distance;
    lastTime = now;
  }

  
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "MODE_THREAT") {
      threatResponse();
    } else if (cmd == "MODE_LOVE") {
      loveResponse();
    }
    neutralPosition();
  }

  delay(50);
}

float measureDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void threatResponse() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(LeftEye, HIGH);
    digitalWrite(RightEye, HIGH);
    servoLeftArm.write(0);
    servoRightArm.write(180);
    delay(100);
    digitalWrite(LeftEye, LOW);
    digitalWrite(RightEye, LOW);
    servoLeftArm.write(90);
    servoRightArm.write(90);
    delay(100);
  }
}

void loveResponse() {
  digitalWrite(LeftEye, HIGH);
  digitalWrite(RightEye, HIGH);
  servoHead.write(60);
  servoLeftArm.write(60);
  servoRightArm.write(120);
  delay(300);
}

void neutralPosition() {
  digitalWrite(LeftEye, LOW);
  digitalWrite(RightEye, LOW);
  servoHead.write(90);
  servoLeftArm.write(90);
  servoRightArm.write(90);
}