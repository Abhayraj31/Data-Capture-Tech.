import paho.mqtt.client as mqtt
from pymongo import MongoClient
import pandas as pd
import time
import json

# MQTT broker details
broker = "2ae91cd025004b64a3e1e8bc34e2e515.s1.eu.hivemq.cloud"  # HiveMQ URL
port = 8883  # Secure MQTT port (TLS)
topic = "gyroscope_data"  # MQTT topic

# MongoDB connection details
mongo_client = MongoClient("mongodb+srv://abhayraj:12345@cluster0.rwxcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB URI
db = mongo_client["Gyroscope_Readings"]  # Database name
collection = db["Gyroscope_Data"]  # Collection name

# Set up the MQTT client
client = mqtt.Client()  # Initialize MQTT client (no callback API version needed)
client.tls_set()  # Enable TLS for secure connection

# Callback when connected to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)  # Subscribe to the specified topic
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when a message is received
def on_message(client, userdata, message):
    try:
        # Decode and parse the MQTT message payload
        data = json.loads(message.payload.decode())
        data["timestamp"] = time.time()  # Add a timestamp
        print(f"Received data: {data}")
        
        # Store the data in MongoDB
        collection.insert_one(data)
    except Exception as e:
        print(f"Error processing message: {e}")

# Configure the MQTT client with callbacks
client = mqtt.Client()
client.username_pw_set("hivemq.webclient.1742209010474", "16xi25EvfFWMO?%B>d;q")  # Set username and password
client.tls_set() 
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port)

# Run the MQTT client and collect data for 30 minutes
print("Starting data collection...")
start_time = time.time()
client.loop_start()  # Start non-blocking loop
while time.time() - start_time < 30 * 60:  # Collect data for 30 minutes
    time.sleep(1)
client.loop_stop()  # Stop the MQTT loop
print("Data collection complete. Check MongoDB for stored data.")

# Step 6: Fetch all data from MongoDB and export to CSV
print("Exporting data to CSV...")
data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's default "_id" field
df = pd.DataFrame(data)  # Convert data to a Pandas DataFrame

# Export raw data to CSV
csv_file = "gyroscope_data.csv"
df.to_csv(csv_file, index=False)
print(f"Raw data exported to {csv_file}")

# Step 7: Clean the data
print("Cleaning data...")
df = df.dropna()  # Remove rows with missing values
df = df[df.applymap(lambda x: isinstance(x, (int, float))).all(1)]  # Keep only numeric rows

# Export cleaned data to a new CSV
cleaned_csv_file = "gyroscope_data_cleaned.csv"
df.to_csv(cleaned_csv_file, index=False)
print(f"Cleaned data exported to {cleaned_csv_file}")


