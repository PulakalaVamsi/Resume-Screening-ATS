from flask import Flask, render_template, request
from utils import *
import os, joblib

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "fit_model.pkl")

ml_model, imputer = None, None
if os.path.exists(MODEL_PATH):
    try:
        ml_model, imputer = joblib.load(MODEL_PATH)
        print("ML model loaded")
    except:
        print("ML model corrupted, retrain required")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        jd = request.form["job_description"]
        file = request.files["resume_file"]

        resume = ""
        if file.filename.endswith(".pdf"):
            resume = extract_text_from_pdf(file)
        elif file.filename.endswith(".docx"):
            resume = extract_text_from_docx(file)

        matched, missing, skill_percent = skill_match(resume, jd)
        resume_exp, jd_exp = experience_match(resume, jd)
        score = final_score(skill_percent, resume_exp, jd_exp)

        save_to_dataset(skill_percent, score)

        if ml_model and imputer:
            features = imputer.transform([[skill_percent, score]])
            fit = ml_model.predict(features)[0]
        else:
            fit = "Rule Based"

        result = {
            "matched": matched,
            "missing": missing,
            "skill_percent": skill_percent,
            "resume_exp": resume_exp,
            "jd_exp": jd_exp,
            "score": score,
            "fit": fit
        }

    return render_template("template.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
