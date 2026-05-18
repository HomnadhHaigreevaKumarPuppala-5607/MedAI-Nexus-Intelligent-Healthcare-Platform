from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "medai_nexus.db"

# CREATE TABLE
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient_name TEXT,
        age INTEGER,
        gender TEXT,

        bp INTEGER,
        glucose INTEGER,
        bmi REAL,
        cholesterol INTEGER,

        smoking_status TEXT,

        predicted_disease TEXT,
        risk_percentage REAL,
        risk_level TEXT,

        doctor_suggestion TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    age = int(data.get("age", 0))
    bp = int(data.get("bp", 0))
    glucose = int(data.get("glucose", 0))
    bmi = float(data.get("bmi", 0))
    cholesterol = int(data.get("cholesterol", 0))
    smoking_status = data.get("smoking_status", "")

    predicted_disease = "No Disease Detected"
    risk_percentage = 8
    risk_level = "Low Risk"
    doctor_suggestion = "Maintain healthy lifestyle"

    if glucose > 126:
        predicted_disease = "Diabetes"
        risk_percentage = 75
        risk_level = "High Risk"
        doctor_suggestion = "Consult diabetologist"

    elif bp > 140 or cholesterol > 240:
        predicted_disease = "Heart Disease"
        risk_percentage = 70
        risk_level = "High Risk"
        doctor_suggestion = "Consult cardiologist"

    elif bmi > 35:
        predicted_disease = "Liver Disease"
        risk_percentage = 60
        risk_level = "Medium Risk"
        doctor_suggestion = "Reduce weight and avoid alcohol"

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patient_analysis (
        patient_name,
        age,
        gender,
        bp,
        glucose,
        bmi,
        cholesterol,
        smoking_status,
        predicted_disease,
        risk_percentage,
        risk_level,
        doctor_suggestion
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Patient",
        age,
        "Male",
        bp,
        glucose,
        bmi,
        cholesterol,
        smoking_status,
        predicted_disease,
        risk_percentage,
        risk_level,
        doctor_suggestion
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "predicted_disease": predicted_disease,
        "risk_percentage": risk_percentage,
        "risk_level": risk_level
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
