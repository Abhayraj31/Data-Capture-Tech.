#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <Arduino_LSM6DS3.h>

// WiFi credentials
const char* ssid = "A";
const char* password = "qwertyui";

// HiveMQ MQTT credentials
const char* mqttServer = "2ae91cd025004b64a3e1e8bc34e2e515.s1.eu.hivemq.cloud";
const int mqttPort = 8883;
const char* mqttUser = "hivemq.webclient.1742209010474";
const char* mqttPassword = "16xi25EvfFWMO?%B>d;q";  
const char* mqttTopic = "gyroscope_data";


WiFiSSLClient wifiClient;  
PubSubClient client(wifiClient);

void connectToWiFi() {
    Serial.print("Connecting to WiFi: ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);

    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED) {
        attempts++;
        Serial.print(".");
        delay(1000);
        if (attempts > 20) {
            Serial.println("\nFailed to connect to WiFi. Retrying...");
            delay(5000);
            return;  
        }
    }
    Serial.println("\nConnected to WiFi!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
}

void connectToMQTT() {
    if (!client.connected()) {
        Serial.println("Setting MQTT server...");
        client.setServer(mqttServer, mqttPort);  

        Serial.println("Connecting to MQTT...");
        if (client.connect("ArduinoClient", mqttUser, mqttPassword)) {
            Serial.println("Connected to MQTT!");
        } else {
            Serial.print("MQTT connection failed. Error Code: ");
            Serial.println(client.state());  
            Serial.println("Retrying in 5 seconds...");
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    delay(2000);  

    connectToWiFi();
    connectToMQTT();

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
}

void loop() {
    if (WiFi.status() != WL_CONNECTED) {
        Serial.println("WiFi disconnected! Trying to reconnect...");
        connectToWiFi();
    }

    connectToMQTT();  
    client.loop();  

    float x, y, z;
    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(x, y, z);

        char payload[100];
        sprintf(payload, "{\"x\":%.2f, \"y\":%.2f, \"z\":%.2f}", x, y, z);
        client.publish(mqttTopic, payload);

        Serial.println(payload);
    }

    delay(5000);  
}






