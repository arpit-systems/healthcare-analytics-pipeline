from pyspark.sql import SparkSession

# STEP 1: Create Spark Session

spark = SparkSession.builder \
    .appName("Healthcare Big Data Pipeline") \
    .getOrCreate()

print("Spark Session Started Successfully")

# STEP 2: Read Healthcare CSV

df = spark.read.csv(
    "../data/patients.csv",
    header=True,
    inferSchema=True
)

print("\nHealthcare Dataset Loaded Using Spark")

# STEP 3: Show Dataset

df.show()

# STEP 4: Print Schema

print("\nDataset Schema")

df.printSchema()

# STEP 5: Total Patients

total_patients = df.count()

print(f"\nTotal Patients: {total_patients}")