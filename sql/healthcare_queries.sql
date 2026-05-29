SELECT disease, COUNT(*) AS total_patients
FROM fact_patient_visits
GROUP BY disease;

SELECT city, COUNT(*) AS total_patients
FROM fact_patient_visits
GROUP BY city;