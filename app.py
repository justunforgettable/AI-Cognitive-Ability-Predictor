import streamlit as st
import pandas as pd
import numpy as np
import joblib

from questions import questions

# ML model

model = joblib.load(
    "cognitive_model.pkl"
)


feature_names = joblib.load(
    "feature_names.pkl"
)

st.set_page_config(
    page_title="CogniScore AI",
    page_icon="🧠",
    layout="centered"
)


st.title("🧠 CogniScore AI")

st.write(
"""
AI-based cognitive ability assessment.
Answer the following reasoning questions
to estimate your cognitive level.
"""
)

name = st.text_input(
    "Enter your name"
)


age = st.number_input(
    "Enter your age",
    min_value=10,
    max_value=100
)
answers = []


for i,q in enumerate(questions):

    st.subheader(
        f"Question {i+1}"
    )

    choice = st.radio(
        q["question"],
        q["options"],
        key=i
    )

    answers.append(
        choice
    )


def process_answers(answers):

    result = {}

    correct = 0


    for i,ans in enumerate(answers):

        if ans == questions[i]["answer"]:
            result[f"Q{i+1}"] = 1
            correct += 1

        else:
            result[f"Q{i+1}"] = 0


    result["total_correct"] = correct


    return result


if st.button("Predict Cognitive Level"):


    data = process_answers(
        answers
    )


    input_df = pd.DataFrame(
        [data]
    )


    prediction = model.predict(
        input_df
    )


    level = prediction[0]


    levels = {
        0:"Developing",
        1:"Average",
        2:"Above Average",
        3:"Advanced",
        4:"Exceptional"
    }


    st.success(
        f"""
        {name}, your cognitive level is:

        ## {levels[level]}
        """
    )




