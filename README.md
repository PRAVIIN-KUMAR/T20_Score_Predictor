# 🏏 T20 Cricket Score Predictor

A machine learning application that predicts the final score of a T20 cricket innings using in-match statistics like current score, overs completed, and last 5 overs runs. Built with `Streamlit`, `scikit-learn`, and `XGBoost`.

## 🌐 Live App

👉 [Try the live app here](https://t20scorepredictor-hvdxregmtfyzluqpfycdxk.streamlit.app/)  

---

## 🎯 Objective

Predict the total runs a team is likely to score in a T20 match based on current in-game conditions using ensemble machine learning models.

---

## 🔍 Features

- Input parameters:
  - Batting & bowling teams
  - City/venue
  - Current score
  - Overs completed
  - Wickets fallen
  - Runs in last 5 overs
- Predicts final score using trained ML model
- Uses `RandomForestRegressor` and/or `XGBRegressor` under a pipeline with preprocessing

---

## ⚙️ How It Works

1. **Data Preprocessing**
   - Categorical encoding using `OneHotEncoder`
   - Numerical features scaled via `StandardScaler`

2. **Model Pipeline**
   - Built using `ColumnTransformer` and `Pipeline`
   - Trained using `RandomForestRegressor` and/or `XGBRegressor`
   - Saved using `pickle` as `pipe.pkl`

3. **Prediction**
   - Features collected from the user
   - Real-time prediction made with the trained model

---


