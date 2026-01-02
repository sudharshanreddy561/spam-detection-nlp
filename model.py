import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("sales.csv")

X = data[["month"]]
y = data["sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next month
next_month = [[13]]
prediction = model.predict(next_month)

print("📊 Sales Forecast")
print("Predicted sales for month 13:", int(prediction[0]))
