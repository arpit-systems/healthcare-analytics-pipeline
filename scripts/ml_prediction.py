import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# Load BIG dataset
df = pd.read_csv("../data/healthcare_big_data.csv")

# Convert dates
df["admission_date"] = pd.to_datetime(df["admission_date"])
df["discharge_date"] = pd.to_datetime(df["discharge_date"])

# Create Length of Stay
df["length_of_stay"] = (
    df["discharge_date"] - df["admission_date"]
).dt.days

# Encode categorical columns
gender_encoder = LabelEncoder()
disease_encoder = LabelEncoder()
city_encoder = LabelEncoder()

df["gender"] = gender_encoder.fit_transform(df["gender"])
df["disease"] = disease_encoder.fit_transform(df["disease"])
df["city"] = city_encoder.fit_transform(df["city"])

# Features
X = df[
    [
        "age",
        "gender",
        "disease",
        "city",
        "hospital_bill",
        "sugar_level",
        "heart_rate"
    ]
]

# Target
y = df["length_of_stay"]

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

# Train Model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("=" * 60)
print("HEALTHCARE LENGTH OF STAY PREDICTION MODEL")
print("=" * 60)

print(f"\nDataset Size: {len(df)} Records")
print(f"Mean Absolute Error: {round(mae,2)}")

print("\nSample Predictions:\n")

for actual, predicted in zip(y_test.head(10), predictions[:10]):
    print(
        f"Actual Stay: {actual} days | Predicted Stay: {round(predicted,2)} days"
    )