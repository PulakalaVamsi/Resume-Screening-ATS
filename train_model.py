import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
import joblib
import os

if not os.path.exists("dataset.csv"):
    print("Run app.py and submit data first")
    exit()

df = pd.read_csv("dataset.csv")

df = df.dropna(subset=["skill_percentage", "final_score"])

if len(df) < 2:
    print("Need at least 2 records to train ML model")
    exit()

def label(score):
    if score >= 80:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Low"

df["label"] = df["final_score"].apply(label)

X = df[["skill_percentage", "final_score"]]
y = df["label"]

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

model = LogisticRegression(max_iter=200)
model.fit(X, y)

joblib.dump((model, imputer), "fit_model.pkl")
print("ML model trained successfully")
