import pandas as pd
from sqlalchemy import create_engine, text

database_url = "postgresql://airflow:airflow123@healthcare-db.cr8mwuquuzbk.ap-south-1.rds.amazonaws.com:5432/postgres"

engine = create_engine(database_url)

df = pd.read_csv("../data/patients.csv")

with engine.connect() as conn:

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_patient (
            patient_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            gender VARCHAR(20),
            city VARCHAR(100)
        );
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_disease (
            disease_id SERIAL PRIMARY KEY,
            disease_name VARCHAR(100) UNIQUE
        );
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_date (
            date_id SERIAL PRIMARY KEY,
            admission_date DATE,
            month INT,
            year INT
        );
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS fact_patient_visits (
            visit_id SERIAL PRIMARY KEY,
            patient_id VARCHAR(20),
            disease VARCHAR(100),
            hospital_bill INT,
            admission_date DATE,
            discharge_date DATE
        );
    """))

    conn.commit()

dim_patient = df[
    ["patient_id", "name", "age", "gender", "city"]
].drop_duplicates()

dim_patient.to_sql(
    "dim_patient",
    engine,
    if_exists="append",
    index=False
)

dim_disease = pd.DataFrame(
    df["disease"].drop_duplicates(),
    columns=["disease"]
)

dim_disease.columns = ["disease_name"]

dim_disease.to_sql(
    "dim_disease",
    engine,
    if_exists="append",
    index=False
)

df["admission_date"] = pd.to_datetime(df["admission_date"])

dim_date = pd.DataFrame()

dim_date["admission_date"] = df["admission_date"]
dim_date["month"] = df["admission_date"].dt.month
dim_date["year"] = df["admission_date"].dt.year

dim_date = dim_date.drop_duplicates()

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)

fact_table = df[
    [
        "patient_id",
        "disease",
        "hospital_bill",
        "admission_date",
        "discharge_date"
    ]
]

fact_table.to_sql(
    "fact_patient_visits",
    engine,
    if_exists="append",
    index=False
)

print("Star Schema Data Warehouse Loaded Successfully")