import pandas as pd

CATEGORY_TOTALS = {
    "Numerical": 3,
    "Logical": 3,
    "Pattern": 3,
    "Verbal": 2,
    "Analytical": 2,
    "Reflection": 2
}


def create_features(user_answers, questions):

    features = {}

    category_scores = {
        "Numerical": 0,
        "Logical": 0,
        "Pattern": 0,
        "Verbal": 0,
        "Analytical": 0,
        "Reflection": 0
    }

    total_correct = 0
    weighted_score = 0

    for i, question in enumerate(questions):

        correct = int(user_answers[i] == question["answer"])

        features[f"Q{i+1}"] = correct

        if correct:
            total_correct += 1
            weighted_score += question["weight"]
            category_scores[question["category"]] += 1

    features["total_correct"] = total_correct

    for category, total in CATEGORY_TOTALS.items():

        features[f"{category}_score"] = (
            category_scores[category] / total
        )

    features["weighted_score"] = weighted_score

    return pd.DataFrame([features])
