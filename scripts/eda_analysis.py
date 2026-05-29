import pandas as pd

df = pd.read_csv("../data/healthcare_big_data.csv")

print("=" * 50)
print("EDA REPORT")
print("=" * 50)

print("\nTotal Records:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDisease Distribution:")
print(df["disease"].value_counts())

print("\nGender Distribution:")
print(df["gender"].value_counts())

print("\nCity Distribution:")
print(df["city"].value_counts())

print("\nAdmission Status Distribution:")
print(df["admission_status"].value_counts())

print("\nAverage Treatment Cost:")
print(round(df["treatment_cost"].mean(), 2))

print("\nMaximum Treatment Cost:")
print(df["treatment_cost"].max())

print("\nMinimum Treatment Cost:")
print(df["treatment_cost"].min())

print("\nEDA Completed Successfully")