import joblib

feature_names = joblib.load("feature_names.pkl")

print(feature_names)
print(len(feature_names))

import streamlit as st
import pandas as pd
import joblib

from questions import questions

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="CogniScore AI",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------
try:
    model = joblib.load("cognitive_model.pkl")
    feature_names = joblib.load("feature_names.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -------------------------------
# Title
# -------------------------------
st.title("🧠 CogniScore AI")

st.markdown("""
### AI Cognitive Ability Assessment

Answer all 15 questions carefully.

**Note:** This project is for educational purposes only and is **not** an official IQ test.
""")

# -------------------------------
# User Details
# -------------------------------
name = st.text_input("Enter Your Name")

age = st.number_input(
    "Enter Your Age",
    min_value=15,
    max_value=80,
    value=20
)

st.divider()

# -------------------------------
# Collect Answers
# -------------------------------
answers = []

for i, q in enumerate(questions):

    st.subheader(f"Question {i+1}")

    choice = st.radio(
        q["question"],
        q["options"],
        key=f"Q{i+1}"
    )

    answers.append(choice)

# -------------------------------
# Feature Engineering
# -------------------------------
def create_features(user_answers):

    result = {}

    category_scores = {
        "Numerical": 0,
        "Logical": 0,
        "Pattern": 0,
        "Verbal": 0,
        "Analytical": 0,
        "Reflection": 0
    }

    category_totals = {
        "Numerical": 3,
        "Logical": 3,
        "Pattern": 3,
        "Verbal": 2,
        "Analytical": 2,
        "Reflection": 2
    }

    total_correct = 0
    weighted_score = 0

    for i, q in enumerate(questions):

        correct = int(user_answers[i] == q["answer"])

        result[f"Q{i+1}"] = correct

        if correct:
            total_correct += 1
            weighted_score += q["weight"]
            category_scores[q["category"]] += 1

    result["total_correct"] = total_correct

    for category in category_scores:
        result[f"{category}_score"] = (
            category_scores[category] /
            category_totals[category]
        )

    result["weighted_score"] = weighted_score

    return result

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Cognitive Level"):

    feature_dict = create_features(answers)

    input_df = pd.DataFrame([feature_dict])

    try:

        input_df = input_df[feature_names]

        prediction = model.predict(input_df)[0]

    except Exception as e:

        st.error("Prediction Error")
        st.exception(e)
        st.write("Input Columns:")
        st.write(input_df.columns.tolist())
        st.write("Expected Columns:")
        st.write(feature_names)
        st.stop()

    levels = {
        0: "Developing",
        1: "Average",
        2: "Above Average",
        3: "Advanced",
        4: "Exceptional"
    }

    st.success(f"### {name}, your Cognitive Level is: **{levels[prediction]}**")

    st.divider()

    st.subheader("Assessment Report")

    correct = feature_dict["total_correct"]

    percentage = round(correct / len(questions) * 100, 1)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Correct Answers", f"{correct}/{len(questions)}")

    with col2:
        st.metric("Score", f"{percentage}%")

    st.subheader("Category Performance")

    categories = [
        "Numerical",
        "Logical",
        "Pattern",
        "Verbal",
        "Analytical",
        "Reflection"
    ]

    for category in categories:

        score = feature_dict[f"{category}_score"]

        st.write(category)
        st.progress(float(score))

    st.subheader("Recommendation")

    if prediction == 4:

        st.success(
            "Outstanding performance. Continue solving advanced reasoning and analytical problems."
        )

    elif prediction == 3:

        st.info(
            "Very good reasoning skills. Practice higher-level logical puzzles to improve further."
        )

    elif prediction == 2:

        st.warning(
            "Good foundation. Focus on numerical reasoning and pattern recognition to improve."
        )

    elif prediction == 1:

        st.warning(
            "Average cognitive performance. Daily reasoning practice can improve your score."
        )

    else:

        st.error(
            "Develop your reasoning skills through puzzles, mathematics, reading, and memory exercises."
        )
