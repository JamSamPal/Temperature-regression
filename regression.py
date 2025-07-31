import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load weather data CSV
df = pd.read_csv('weather_data.csv')

df['date'] = pd.to_datetime(df['date'])
df['hour'] = df['date'].dt.hour

features = ['humidity', 'pressure', 'wind_speed', 'hour']
X = df[features]
y = df['temperature']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse:.2f}")
