import streamlit as st
import pandas as pd
import joblib

from questions import questions
model = joblib.load("cognitive_model.pkl")
feature_names = joblib.load("feature_names.pkl")

def create_features(user_answers):

    result = {}

    category_scores = {
        "Numerical":0,
        "Logical":0,
        "Pattern":0,
        "Verbal":0,
        "Analytical":0,
        "Reflection":0
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

    result["Numerical_score"] = category_scores["Numerical"]/3
    result["Logical_score"] = category_scores["Logical"]/3
    result["Pattern_score"] = category_scores["Pattern"]/3
    result["Verbal_score"] = category_scores["Verbal"]/2
    result["Analytical_score"] = category_scores["Analytical"]/2
    result["Reflection_score"] = category_scores["Reflection"]/2

    result["weighted_score"] = weighted_score


feature_dict = create_features(user_answers)

input_df = pd.DataFrame([feature_dict])

input_df = input_df[feature_names]

prediction = model.predict(input_df)[0]

input_df = input_df[feature_names]


levels = {
    0:"Developing",
    1:"Average",
    2:"Above Average",
    3:"Advanced",
    4:"Exceptional"
}

st.success(f"Predicted Level: {levels[prediction]}")


return result
