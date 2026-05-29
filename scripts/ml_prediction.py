import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# Load Dataset

df = pd.read_csv("../data/healthcare_big_data.csv")

# Encode categorical columns

gender_encoder = LabelEncoder()
disease_encoder = LabelEncoder()
city_encoder = LabelEncoder()
status_encoder = LabelEncoder()

df["gender"] = gender_encoder.fit_transform(df["gender"])
df["disease"] = disease_encoder.fit_transform(df["disease"])
df["city"] = city_encoder.fit_transform(df["city"])
df["admission_status"] = status_encoder.fit_transform(
    df["admission_status"]
)

# Features

X = df[
    [
        "age",
        "gender",
        "disease",
        "city",
        "admission_status"
    ]
]

# Target

y = df["treatment_cost"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train

model.fit(X_train, y_train)

# Predict

predictions = model.predict(X_test)

# Evaluate

mae = mean_absolute_error(y_test, predictions)

print("=" * 60)
print("HEALTHCARE TREATMENT COST PREDICTION MODEL")
print("=" * 60)

print(f"\nDataset Size: {len(df)} Records")
print(f"Mean Absolute Error: {round(mae,2)}")

print("\nSample Predictions:\n")

for actual, predicted in zip(y_test.head(10), predictions[:10]):
    print(
        f"Actual Cost: ₹{actual} | Predicted Cost: ₹{round(predicted,2)}"
    )

print("\nModel Training Completed Successfully")