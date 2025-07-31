import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

# Load weather data CSV
df = pd.read_csv('./weatherHistory.csv')

df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], errors='coerce', utc=True)
df['hour'] = df['Formatted Date'].dt.hour

# Add a feature corresponding to the temperature at the same time on the previous day
df['temp_lag_24'] = df['Temperature (C)'].shift(24)

# Drop rows with NaN in lag columns
df = df.dropna(subset=['temp_lag_24'])

features = ['Humidity', 'Wind Speed (km/h)', 'temp_lag_24', 'hour']
X = df[features]
y = df['Temperature (C)']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Plot
plt.figure(figsize=(6, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
plt.xlabel('Actual Temperature')
plt.ylabel('Predicted Temperature')
plt.title('Predicted vs Actual Temperature')
plt.show()


# Distribution of errors
errors = y_test - y_pred
plt.figure(figsize=(8, 5))
sns.histplot(errors, bins=30, kde=True)
plt.title('Distribution of Prediction Errors')
plt.xlabel('Prediction Error (Actual - Predicted)')
plt.show()

# Evaluation of performance
rmse = root_mean_squared_error(y_test, y_pred)
print(f"RMSE: {rmse:.2f}")

