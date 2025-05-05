import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = "sensor_data.csv"
try:
    df = pd.read_csv(file_path, encoding="ISO-8859-1", dtype=str, on_bad_lines='skip')
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Normalize column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Check if required columns exist
required_columns = {"Temperature", "Humidity"}
if not required_columns.issubset(df.columns):
    print(f"Error: Missing required columns. Found columns: {list(df.columns)}")
    exit()

# Extract numeric values from Temperature and Humidity columns
df["Temperature"] = df["Temperature"].str.extract(r'([\d\.]+)').astype(float)
df["Humidity"] = df["Humidity"].str.extract(r'([\d\.]+)').astype(float)

# Drop any rows with NaN values
df = df.dropna()

# Train Linear Regression model
X = df["Temperature"].values.reshape(-1, 1)
y = df["Humidity"].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

# Print model coefficients
print(f"Slope (Coefficient): {model.coef_[0][0]}")
print(f"Intercept: {model.intercept_[0]}")

# Generate 100 equally spaced temperature values for prediction
X_test = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = model.predict(X_test)

# Plot scatter plot and trend line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='green', label='Original Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Trend Line')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Temperature vs Humidity with Linear Regression')
plt.legend()
plt.show()

# Outlier detection based on deviation from trend line
threshold = 5  # Define acceptable deviation range
predicted_y = model.predict(X)
deviation = np.abs(y - predicted_y)
outliers = df[deviation.flatten() > threshold]

# Print outliers
print("Identified Outliers:")
print(outliers)





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = "sensor_data.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1", dtype=str)

# Normalize column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Print available columns for debugging
print("Available columns:", df.columns.tolist())

# Check if required columns exist
if "Temperature" not in df.columns or "Humidity" not in df.columns:
    print("Error: Missing 'Temperature' or 'Humidity' column in the dataset.")
    exit()

# Extract numeric values
df["Temperature"] = df["Temperature"].str.extract(r'([\d\.]+)').astype(float)
df["Humidity"] = df["Humidity"].str.extract(r'([\d\.]+)').astype(float)

# Drop NaN values
df = df.dropna()

# Train Linear Regression model
X = df["Temperature"].values.reshape(-1, 1)
y = df["Humidity"].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

# Print coefficients
print(f"Slope: {model.coef_[0][0]}, Intercept: {model.intercept_[0]}")

# Predict and plot
X_test = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = model.predict(X_test)

plt.scatter(X, y, color='green', label='Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.legend()
plt.show()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
file_path = "sensor_data.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1", dtype=str)

# Print available columns
print("Available columns:", df.columns.tolist())

# Normalize column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Verify column presence
if "Temperature" not in df.columns:
    print("Error: 'Temperature' column not found in CSV. Check file formatting.")
    exit()

# Check first few rows
print(df.head())

# Extract numeric values
df["Temperature"] = df["Temperature"].str.extract(r'([\d\.]+)').astype(float)
df["Humidity"] = df["Humidity"].str.extract(r'([\d\.]+)').astype(float)

# Drop NaN values
df = df.dropna()

# Train Linear Regression model
X = df["Temperature"].values.reshape(-1, 1)
y = df["Humidity"].values.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

# Print regression details
print(f"Slope: {model.coef_[0][0]}, Intercept: {model.intercept_[0]}")

# Plot data
plt.scatter(X, y, color='green', label='Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.legend()
plt.show()
