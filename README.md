# Healthcare Analytics Pipeline Project for MediCare Hospital

## Project Overview

This project is an end-to-end Healthcare Analytics Pipeline developed as an IIT Jodhpur Capstone Project. The pipeline automates healthcare data ingestion, transformation, storage, analytics, machine learning, and dashboard visualization using modern Data Engineering technologies.

The project integrates Python, Pandas, Apache Kafka, Apache Airflow, Databricks, PySpark, PostgreSQL, AWS S3, AWS RDS, Docker, GitHub Actions CI/CD, Machine Learning, and Streamlit to create a scalable healthcare analytics platform.

---

## Live Application

🌐 Dashboard:
https://medicare-healthcare-dashboard.streamlit.app

🎥 Project Demonstration Video:
https://www.youtube.com/watch?v=ZlmjyJwMq88

💻 GitHub Repository:
https://github.com/arpit-systems/healthcare-analytics-pipeline

---

## Objectives

* Build an automated ETL pipeline for healthcare data.
* Store healthcare records in PostgreSQL.
* Automate workflows using Apache Airflow.
* Perform distributed processing using PySpark.
* Integrate AWS S3 and AWS RDS cloud services.
* Design a Star Schema Data Warehouse.
* Generate healthcare insights using SQL analytics.
* Build interactive dashboards using Streamlit.
* Implement Machine Learning for Treatment Cost Prediction.
* Demonstrate real-time healthcare data streaming using Apache Kafka.
* Validate PySpark processing using Databricks notebooks.
* Implement CI/CD automation using GitHub Actions.

---

## Technology Stack

### Data Engineering & ETL

* Python
* Pandas
* Apache Airflow

### Data Streaming

* Apache Kafka

### Big Data Processing & Management

* Apache Spark
* PySpark
* Databricks

### Database & Data Warehousing

* PostgreSQL
* AWS RDS PostgreSQL
* Star Schema Data Warehouse

### Cloud Services

* AWS S3
* AWS RDS

### Machine Learning

* Scikit-Learn
* Random Forest Regressor

### Dashboard & Visualization

* Streamlit
* Matplotlib

### DevOps & MLOps

* Docker
* Docker Compose
* Git
* GitHub
* GitHub Actions (CI/CD)

---

## Architecture

Healthcare Dataset (CSV)

↓

AWS S3 Data Lake

↓

Apache Kafka Streaming Layer

↓

Python ETL Pipeline (Pandas)

↓

Databricks / PySpark Big Data Processing

↓

AWS RDS PostgreSQL

↓

Star Schema Data Warehouse

↓

Apache Airflow Workflow Automation

↓

SQL Analytics Layer

↓

Machine Learning (Random Forest)

↓

Streamlit Dashboard

↓

Healthcare Insights & Reporting

---

## Key Features

* Automated ETL Pipeline
* Cloud Data Storage
* Data Warehouse Implementation
* Distributed Processing using PySpark
* Airflow Workflow Automation
* SQL Analytics
* Interactive Dashboard
* Predictive Modeling
* Healthcare Reporting
* Apache Kafka streaming demonstration
* Databricks notebook integration
* GitHub Actions CI/CD automation

---

## Dashboard Screenshots

The Streamlit dashboard provides interactive healthcare analytics and filter-based visualizations.

### Available Dashboard Views

- Complete Dashboard Overview
- Monthly Admission Trend
- Disease Distribution
- Admission Status Analysis
- Top Treatment Costs
- Filter Analytics (Disease, Gender & City)

Dashboard screenshots are available in the `screenshots` folder of this repository.

---

## Machine Learning Module

A Machine Learning model was implemented to predict treatment cost using healthcare attributes.

### Features Used

* Age
* Gender
* Disease
* City
* Admission Status

### Evaluation Metric

* Mean Absolute Error (MAE)

---

## Exploratory Data Analysis (EDA)

EDA was performed on a healthcare dataset containing 5000 records.

### Analysis Included

* Disease Distribution
* Gender Distribution
* City Distribution
* Admission Status Analysis
* Treatment Cost Analysis
* Missing Value Analysis

---

## Project Structure

healthcare-analytics-pipeline

├── .github

│   └── workflows

│       └── main.yml

├── dashboards

│   ├── app.py

│   └── app_live.py

├── data

│   ├── patients.csv

│   └── healthcare_big_data.csv

├── docker_airflow

│   ├── dags

│   │   └── healthcare_etl_dag.py

│   └── docker-compose.yml

├── docs

├── kafka_demo

│   ├── producer.py

│   └── consumer.py

├── screenshots

├── scripts

│   ├── etl_pipeline.py

│   ├── spark_pipeline.py

│   ├── data_warehouse.py

│   ├── ml_prediction.py

│   └── eda_analysis.py

├── sql

│   └── healthcare_queries.sql

├── weekly_reports

├── README.md

├── requirements.txt

└── .gitignore

---

## Future Scope

* Enterprise-scale Apache Kafka streaming architecture
* Snowflake Data Warehouse integration
* Advanced Machine Learning models
* Kubernetes-based deployment
* Power BI integration
* Healthcare alerting and monitoring systems

---

## Authors

* Arpit Sharma (G25AI1012)
* Ankita Dwivedi (G25AI1011)
* Astosh Ranjan (G25AI1013)
* Bharat Sharma (G25AI1014)
* Damini Khatri (G25AI1015)

---

## Institution

IIT Jodhpur PGDDE Capstone Project

Healthcare Analytics Pipeline for MediCare Hospital

