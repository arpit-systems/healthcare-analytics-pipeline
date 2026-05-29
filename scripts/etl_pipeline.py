import pandas as pd
from sqlalchemy import create_engine

# STEP 1: Read CSV File

df = pd.read_csv("../data/patients.csv")

print("Healthcare Dataset Loaded Successfully")

print(df.head())

# STEP 2: Basic Data Cleaning

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

print("\nData Cleaning Completed")

# STEP 3: PostgreSQL Connection

database_url = "postgresql://airflow:airflow123@healthcare-db.cr8mwuquuzbk.ap-south-1.rds.amazonaws.com:5432/postgres"

engine = create_engine(database_url)

print("\nPostgreSQL Connection Successful")

# STEP 4: Load Data into PostgreSQL

df.to_sql(
    name="patients",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nData Loaded into PostgreSQL Successfully")