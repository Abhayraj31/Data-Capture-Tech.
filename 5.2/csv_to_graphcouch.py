import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "gyroscopedata.csv"
df = pd.read_csv(file_path)

# Generate a timestamp assuming regular intervals
df['timestamp'] = pd.RangeIndex(start=0, stop=len(df), step=1)

# Plot the gyroscope data
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['x'], label='X-axis')
plt.plot(df['timestamp'], df['y'], label='Y-axis')
plt.plot(df['timestamp'], df['z'], label='Z-axis')
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Gyroscope Reading')
plt.title('Gyroscope Readings Over Time')
plt.legend()
plt.grid()
plt.show()

