import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
csv_filename = "gyroscope_data_cleaned.csv"
df = pd.read_csv(csv_filename)

# Convert timestamp to datetime format (if not already converted)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Plot Graph
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["x"], label="X-axis", color="r")
plt.plot(df["timestamp"], df["y"], label="Y-axis", color="g")
plt.plot(df["timestamp"], df["z"], label="Z-axis", color="b")

# Formatting
plt.xlabel("Timestamp")
plt.ylabel("Gyroscope Readings")
plt.title("Gyroscope Sensor Data Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid()

# Show Graph
plt.show()
    