import pandas as pd
import joblib
import warnings

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

warnings.filterwarnings("ignore")

df = pd.read_csv("Training.csv")

print("Dataset Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Check target column
if "prognosis" not in df.columns:
    print("ERROR: prognosis column not found.")
    print("Your columns are:", df.columns.tolist())
    exit()

# Check dataset size
if df.shape[0] < 1000:
    print("\nWARNING: This file is too small.")
    print("You are probably using Testing.csv.")
    print("Download correct Training.csv with around 4920 rows.")
    exit()

# Clean target
df["prognosis"] = df["prognosis"].astype(str).str.strip()

X = df.drop("prognosis", axis=1)
y = df["prognosis"]

print("Total Diseases:", y.nunique())
print("Total Rows:", len(df))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

print("\nTraining Started...")

model.fit(X_train, y_train)

print("Model Trained Successfully!")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")

joblib.dump(model, "disease_model.pkl")
joblib.dump(list(X.columns), "symptom_columns.pkl")

print("Model Saved Successfully!")