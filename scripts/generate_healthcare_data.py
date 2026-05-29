import pandas as pd
import random
from faker import Faker

fake = Faker()

# Lists
diseases = [
    "COVID",
    "DIABETES",
    "ASTHMA",
    "HYPERTENSION",
    "CANCER",
    "HEART DISEASE"
]

cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Pune",
    "Chennai",
    "Hyderabad"
]

genders = [
    "Male",
    "Female"
]

admission_status = [
    "Admitted",
    "Discharged"
]

# Store records
data = []

# Generate 5000 patients
for i in range(1, 5001):

    patient = {
        "patient_id": i,
        "patient_name": fake.name(),
        "age": random.randint(1, 90),
        "gender": random.choice(genders),
        "disease": random.choice(diseases),
        "city": random.choice(cities),
        "treatment_cost": random.randint(5000, 200000),
        "admission_status": random.choice(admission_status),
        "admission_date": fake.date_between(
            start_date="-1y",
            end_date="today"
        )
    }

    data.append(patient)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv(
    "data/healthcare_big_data.csv",
    index=False
)

print("5000 Healthcare Records Generated Successfully")