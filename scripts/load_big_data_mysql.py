import pandas as pd
import mysql.connector

print("Loading 5000 Healthcare Records Into MySQL")

# Read CSV file
df = pd.read_csv(
    "data/healthcare_big_data.csv"
)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="healthcare_db"
)

cursor = connection.cursor()

# SQL Insert Query
sql_query = """
INSERT INTO healthcare_records (

    patient_id,
    patient_name,
    age,
    gender,
    disease,
    city,
    treatment_cost,
    admission_status,
    admission_date

)

VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert Data
for index, row in df.iterrows():

    values = (

        int(row["patient_id"]),
        row["patient_name"],
        int(row["age"]),
        row["gender"],
        row["disease"],
        row["city"],
        int(row["treatment_cost"]),
        row["admission_status"],
        row["admission_date"]

    )

    cursor.execute(sql_query, values)

# Save Changes
connection.commit()

print("5000 Records Loaded Successfully")

# Close Connection
cursor.close()
connection.close()