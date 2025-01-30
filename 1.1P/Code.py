import serial
import random
import time
from datetime import datetime


ser = serial.Serial('COM14', 9600, timeout=1)
time.sleep(2)  

def log(message):
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

while True:
    
    number_to_send = random.randint(1, 10)
    ser.write(f"{number_to_send}\n".encode())  
    log(f"Sent: {number_to_send}")

    
    while True:
        response = ser.readline().decode().strip()  
        if response.isdigit():  
            delay_time = int(response)
            log(f"Received: {delay_time}")
            break  

    
    log(f"Sleeping for {delay_time} seconds...")
    time.sleep(delay_time)
