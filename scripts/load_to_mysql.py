import pandas as pd
import mysql.connector

print("Healthcare ETL Load Process Started")

# Read CSV file
df = pd.read_csv("data/patients.csv")

# Data Cleaning
df = df.drop_duplicates()

df["age"] = df["age"].fillna(df["age"].mean())

df["disease"] = df["disease"].str.upper()

df["city"] = df["city"].str.title()

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="healthcare_db"
)

cursor = connection.cursor()

# Insert data into MySQL
for index, row in df.iterrows():

    sql_query = """
    INSERT INTO patients
    (patient_id, patient_name, age, disease, city)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        int(row["patient_id"]),
        row["patient_name"],
        float(row["age"]),
        row["disease"],
        row["city"]
    )

    cursor.execute(sql_query, values)

# Save changes
connection.commit()

print("Data Loaded Successfully Into MySQL")

# Close connection
cursor.close()
connection.close()