import paho.mqtt.client as mqtt
import couchdb
import json

#  HiveMQ Cloud MQTT Broker Settings
MQTT_BROKER = "2ae91cd025004b64a3e1e8bc34e2e515.s1.eu.hivemq.cloud"
MQTT_PORT = 8883  # Secure port
MQTT_USERNAME = "hivemq.webclient.1742209010474"
MQTT_PASSWORD = "16xi25EvfFWMO?%B>d;q"
MQTT_TOPIC = "gyroscope_data"  # Ensure this matches what Arduino publishes

#  CouchDB Configuration
COUCHDB_URL = "http://abhayraj:abhayraj@localhost:5984/"  # Update credentials if necessary
DATABASE_NAME = "gyroscope"

#  Connect to CouchDB
try:
    couch = couchdb.Server(COUCHDB_URL)
    if DATABASE_NAME in couch:
        db = couch[DATABASE_NAME]
        print(f" Connected to CouchDB. Using database: {DATABASE_NAME}")
    else:
        db = couch.create(DATABASE_NAME)
        print(f" Created new CouchDB database: {DATABASE_NAME}")
except Exception as e:
    print(f" Failed to connect to CouchDB: {e}")
    exit(1)

#  Callback when connected to MQTT
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(" Successfully connected to HiveMQ Cloud!")
        client.subscribe(MQTT_TOPIC)
        print(f" Subscribed to topic: {MQTT_TOPIC}")
    elif rc == 5:
        print(" Connection failed: Not authorized. Check your username/password.")
    else:
        print(f"Connection failed with return code {rc}")

#  Callback when a message is received
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f" Received message: {payload} on topic {msg.topic}")

        # Convert JSON string to Python dictionary
        data = json.loads(payload)

        #  Insert data into CouchDB
        db.save(data)
        print(" Data saved to CouchDB!")

    except Exception as e:
        print(f" Error processing message: {e}")

#  Create MQTT Client
client = mqtt.Client()

# Enable TLS for secure connection
client.tls_set()

# Set Username and Password for HiveMQ
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# Attach Callback Functions
client.on_connect = on_connect
client.on_message = on_message

# Enable Debugging Logs
client.enable_logger()

#  Connect to HiveMQ Cloud
print(" Connecting to HiveMQ Cloud...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)

#  Keep the client running
client.loop_forever()