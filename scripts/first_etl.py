import pandas as pd

print("Healthcare ETL Pipeline Started")

# Read CSV file
df = pd.read_csv("data/patients.csv")

print("\nOriginal Dataset:\n")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing age values with average age
df["age"] = df["age"].fillna(df["age"].mean())

# Standardize disease names
df["disease"] = df["disease"].str.upper()

# Standardize city names
df["city"] = df["city"].str.title()

print("\nCleaned Dataset:\n")
print(df)

print("\nDataset Information:\n")
print(df.info())