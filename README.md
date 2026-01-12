📌 Intelligent Resume Screening System

A Python-based Resume Screening Web Application designed to automate the evaluation of resumes against job descriptions.
The system extracts skills and experience from resumes, calculates a matching score, and predicts candidate suitability using both rule-based logic and Machine Learning.

This project demonstrates practical use of **Python, Flask, Regex, and Machine Learning** to solve a real-world HR automation problem.

---

✨ Features

📄 Resume Upload: Supports PDF and DOCX resume formats.

🧠 Skill Extraction: Automatically extracts technical skills using predefined keywords.

📊 Skill Match Percentage: Calculates how well a resume matches the job description.

🕒 Experience Analysis: Extracts and compares required and actual experience using regex.

🎯 Final Scoring System: Uses weighted logic based on skills and experience.

🤖 Candidate Fit Prediction: Classifies candidates as **Good / Average / Low** using a Logistic Regression model.

💾 Dataset Creation: Stores screening data for continuous ML model improvement.

🌐 Web Interface: Simple and clean UI built using HTML and CSS.

---

🛠️ Tech Stack

Programming Language: Python

Web Framework: Flask

Machine Learning: Scikit-learn (Logistic Regression)

Data Handling: Pandas

Text Processing: Regex

Resume Parsing: PyPDF2, python-docx

Frontend: HTML, CSS

Tools: VS Code, Git, GitHub

---

📂 Project Structure

Resume-Screening-System
│── app.py
│── utils.py
│── train_model.py
│── dataset.csv
│── fit_model.pkl
│
├── templates/
│   └── template.html
│
├── static/
│   └── style.css
│
└── README.md

---

🚀 Getting Started

Prerequisites

* Install Python 3.8 or above
* Install pip package manager
* Basic knowledge of Flask

Steps to Run

Clone the repository:

git clone [https://github.com/your-username/Resume-Screening-System.git](https://github.com/your-username/Resume-Screening-System.git)
cd Resume-Screening-System

Install required libraries:

pip install flask pandas scikit-learn PyPDF2 python-docx joblib

Run the application:

python app.py

Open your browser and visit:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

📊 Scoring Logic

* 75% weight → Skill Match Percentage
* 25% weight → Experience Match

Final Score = Skill Score + Experience Score

---

🤖 Machine Learning Model

Algorithm Used: Logistic Regression

Input Features:

* Skill Match Percentage
* Final Score

Classification Labels:

* **Good** → Score ≥ 80
* **Average** → Score between 50 and 79
* **Low** → Score < 50

---

📖 Learning Outcomes

* Implemented real-world resume screening logic
* Gained hands-on experience with Flask web applications
* Learned resume parsing using PDF and DOCX files
* Applied Machine Learning for classification problems
* Understood HR automation and candidate evaluation systems

---

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request with improvements.

---

📜 License

This project is licensed under the MIT License.

---

⭐ Conclusion

This Resume Screening System showcases the integration of **Web Development, Text Processing, and Machine Learning** to automate candidate evaluation.
It is suitable for academic projects, internships, and entry-level software engineering portfolios.
