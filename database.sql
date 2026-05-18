CREATE DATABASE IF NOT EXISTS medai_nexus_db;

USE medai_nexus_db;

DROP TABLE IF EXISTS patient_analysis;

CREATE TABLE patient_analysis (
    id INT AUTO_INCREMENT PRIMARY KEY,

    patient_name VARCHAR(100),
    age INT NOT NULL,
    gender VARCHAR(20),

    bp INT NOT NULL,
    glucose INT NOT NULL,
    bmi FLOAT NOT NULL,
    cholesterol INT NOT NULL,

    smoking_status VARCHAR(50),

    predicted_disease VARCHAR(100),
    risk_percentage FLOAT,
    risk_level VARCHAR(50),

    doctor_suggestion TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- View all patient details
SELECT * FROM patient_analysis;

-- Latest patient records first
SELECT * FROM patient_analysis
ORDER BY id DESC;

-- High risk patients
SELECT * FROM patient_analysis
WHERE risk_level = 'High Risk';

-- Medium risk patients
SELECT * FROM patient_analysis
WHERE risk_level = 'Medium Risk';

-- Low risk patients
SELECT * FROM patient_analysis
WHERE risk_level = 'Low Risk';

-- No disease detected patients
SELECT * FROM patient_analysis
WHERE predicted_disease = 'No Disease Detected';

-- Diabetes patients
SELECT * FROM patient_analysis
WHERE predicted_disease = 'Diabetes';

-- Heart disease patients
SELECT * FROM patient_analysis
WHERE predicted_disease = 'Heart Disease';

-- Liver disease patients
SELECT * FROM patient_analysis
WHERE predicted_disease = 'Liver Disease';

-- Search patient by name
SELECT * FROM patient_analysis
WHERE patient_name LIKE '%Rahul%';

-- Count total patients
SELECT COUNT(*) AS total_patients
FROM patient_analysis;

-- Count patients by risk level
SELECT risk_level, COUNT(*) AS total
FROM patient_analysis
GROUP BY risk_level;

-- Count patients by disease
SELECT predicted_disease, COUNT(*) AS total
FROM patient_analysis
GROUP BY predicted_disease;

-- Today inserted patient records
SELECT * FROM patient_analysis
WHERE DATE(created_at) = CURDATE();

-- Delete one patient by id
-- Change id number before running
DELETE FROM patient_analysis
WHERE id = 1;