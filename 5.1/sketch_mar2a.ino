#include <Arduino_LSM6DS3.h>

void setup() {
    Serial.begin(115200);
    while (!Serial);
    
    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
    
    Serial.println("Gyroscope data collection started...");
}

void loop() {
    float x, y, z;
    
    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(x, y, z);
        
        // Send data as JSON format
        Serial.print("{\"x\":");
        Serial.print(x);
        Serial.print(", \"y\":");
        Serial.print(y);
        Serial.print(", \"z\":");
        Serial.print(z);
        Serial.print(", \"timestamp\":");
        Serial.print(millis());
        Serial.println("}");
    }
    
    delay(100); // Adjust sample rate as needed
}
