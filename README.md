# 🧠 CogniScore AI

An AI-powered cognitive ability assessment web application built using **Machine Learning** and **Streamlit**. The application evaluates users through 15 reasoning-based questions and predicts their cognitive ability level based on their responses.

## 🚀 Live Demo

**Application:** https://ai-cognitive-ability-predictor-fi3pukn7gnjv2qfdcnjzao.streamlit.app/

## ✨ Features

* 15 reasoning-based assessment questions
* Machine Learning-based cognitive level prediction
* Category-wise performance analysis
* Instant assessment report
* Simple and responsive Streamlit interface
* Educational demonstration of ML model deployment

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

## 📂 Project Structure

```
AI-Cognitive-Ability-Predictor/
│── app.py
│── questions.py
│── cognitive_model.pkl
│── feature_names.pkl
│── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd AI-Cognitive-Ability-Predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🧠 Machine Learning Workflow

1. Users answer 15 cognitive reasoning questions.
2. Responses are converted into engineered features.
3. The trained Random Forest model predicts the cognitive ability level.
4. The application displays the predicted level along with category-wise performance.

## 📊 Predicted Levels

* Developing
* Average
* Above Average
* Advanced
* Exceptional

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. It is **not** an officially validated IQ test or a clinical psychological assessment.

## 👩‍💻 Author

**Nahid Kausar**

B.Tech Computer Science Engineering
University College of Engineering and Technology (UCET), Vinoba Bhave University

---

⭐ If you found this project useful, consider giving the repository a star.
