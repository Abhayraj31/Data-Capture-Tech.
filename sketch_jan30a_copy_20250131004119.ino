void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    int blinkCount = Serial.parseInt();  
    if (blinkCount > 0) {
      for (int i = 0; i < blinkCount; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);  
        digitalWrite(LED_BUILTIN, LOW);
        delay(1000);  
      }
      int randomDelay = random(1, 11);  
      Serial.println(randomDelay);      
    }
  }
}

