from pyspark.sql import SparkSession

# STEP 1: Create Spark Session

spark = SparkSession.builder \
    .appName("Healthcare Big Data Pipeline") \
    .getOrCreate()

print("Spark Session Started Successfully")

# STEP 2: Read Healthcare Big Dataset

df = spark.read.csv(
    "../data/healthcare_big_data.csv",
    header=True,
    inferSchema=True
)

print("\nHealthcare Big Dataset Loaded Using Spark")

# STEP 3: Show First 10 Records

print("\nFirst 10 Records")

df.show(10)

# STEP 4: Print Schema

print("\nDataset Schema")

df.printSchema()

# STEP 5: Total Patients

total_patients = df.count()

print(f"\nTotal Patients: {total_patients}")

# STEP 6: Disease Distribution

print("\nDisease Distribution")

df.groupBy("disease").count().show()

# STEP 7: Average Treatment Cost

print("\nAverage Treatment Cost")

df.groupBy().avg("treatment_cost").show()

print("\nPySpark Processing Completed Successfully")

# STEP 8: Stop Spark Session

spark.stop()