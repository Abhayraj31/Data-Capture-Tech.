const int trigpin = 7;
const int echopin = 8;
long duration;
int distance;

void setup() {

  pinMode(trigpin, OUTPUT);
  pinMode(echopin, INPUT);
  Serial.begin(9600);
}

void loop() {

  digitalWrite(trigpin, LOW);
  delayMicroseconds(5);

  digitalWrite(trigpin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigpin, LOW);

  duration = pulseIn(echopin, HIGH);
  distance = duration * 0.034 / 2;

  Serial.print("Distance:");
  
  Serial.println(distance);
  delay(1000);
}