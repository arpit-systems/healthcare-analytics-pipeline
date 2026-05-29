from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine


# -----------------------------------
# TASK 1
# GENERATE HEALTHCARE DATA
# -----------------------------------

def generate_healthcare_data():

    data = {

        "patient_id": [1, 2, 3, 4, 5],

        "patient_name": [
            "Arjun",
            "Riya",
            "Kabir",
            "Meera",
            "Rahul"
        ],

        "disease": [
            "COVID",
            "DIABETES",
            "ASTHMA",
            "CANCER",
            "HYPERTENSION"
        ],

        "treatment_cost": [
            50000,
            70000,
            30000,
            150000,
            60000
        ]

    }

    df = pd.DataFrame(data)

    df.to_csv(
        "/opt/airflow/dags/healthcare_data.csv",
        index=False
    )

    print("Healthcare CSV Generated Successfully")


# -----------------------------------
# TASK 2
# LOAD DATA INTO POSTGRESQL
# -----------------------------------

def load_data_to_postgres():

    df = pd.read_csv(
        "/opt/airflow/dags/healthcare_data.csv"
    )

    engine = create_engine(
        "postgresql+psycopg2://airflow:airflow@postgres/airflow"
    )

    df.to_sql(
        "healthcare_records",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data Loaded Into PostgreSQL Successfully")


# -----------------------------------
# DAG
# -----------------------------------

with DAG(

    dag_id="healthcare_etl_pipeline",

    start_date=datetime(2024, 1, 1),

    schedule="@daily",

    catchup=False

) as dag:

    task1 = PythonOperator(

        task_id="generate_healthcare_data",

        python_callable=generate_healthcare_data

    )

    task2 = PythonOperator(

        task_id="load_data_to_postgres",

        python_callable=load_data_to_postgres

    )

    task1 >> task2