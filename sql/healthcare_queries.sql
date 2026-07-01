-- Gender distribution
SELECT gender, COUNT(*) AS total_patients
FROM fact_patient_visits
GROUP BY gender;

-- Admission status distribution
SELECT admission_status, COUNT(*) AS total_patients
FROM fact_patient_visits
GROUP BY admission_status;

-- Monthly admission trend
SELECT DATE_TRUNC('month', admission_date) AS admission_month,
       COUNT(*) AS total_patients
FROM fact_patient_visits
GROUP BY admission_month
ORDER BY admission_month;

-- Top treatment costs
SELECT patient_id,
       patient_name,
       disease,
       city,
       treatment_cost
FROM fact_patient_visits
ORDER BY treatment_cost DESC
LIMIT 10;

-- Average treatment cost by disease
SELECT disease,
       ROUND(AVG(treatment_cost),2) AS avg_treatment_cost
FROM fact_patient_visits
GROUP BY disease
ORDER BY avg_treatment_cost DESC;

-- Total revenue by city
SELECT city,
       SUM(treatment_cost) AS total_revenue
FROM fact_patient_visits
GROUP BY city
ORDER BY total_revenue DESC;
