import pandas as pd
import matplotlib.pyplot as plt

filename = "Readings.csv"
df = pd.read_csv(filename)

df['Timestamp'] = pd.to_datetime(df['Time'], format="%Y%m%d%H%M%S")

df['Distance in (cm)'] = df['Distance in (cm)'].astype(str).str.extract(r'(\d+)')

df['Smoothed_Distance'] = df['Distance in (cm)'].rolling(window=5, min_periods=1).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['Smoothed_Distance'], markersize=1, linestyle='-', color='b')
plt.xlabel('Time')
plt.ylabel('Distance (cm)')
plt.title('Ultrasonic Sensor Readings (Smoothed)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()