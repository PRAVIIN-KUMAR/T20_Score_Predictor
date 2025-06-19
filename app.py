import streamlit as st
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from PIL import Image


# Page settings
st.set_page_config(page_title="T20 Score Predictor", layout="wide")

# Load the trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Teams and cities
teams = ['West Indies', 'Pakistan', 'India', 'South Africa', 'England', 'Australia', 'New Zealand', 'Sri Lanka', 'Bangladesh']

cities = sorted([
    'Colombo', 'Dubai', 'Johannesburg', 'Mirpur', 'Auckland', 'Sydney', 'Cape Town', 'Dhaka', 'Lahore', 'London',
    'Durban', 'Melbourne', 'Pallekele', 'Wellington', 'Barbados', 'Centurion', 'Christchurch', 'Lauderhill',
    'Abu Dhabi', 'Mount Maunganui', 'Southampton', 'Gros Islet', 'Manchester', 'Nottingham', 'St Lucia', 'Karachi',
    'Kolkata', 'Hamilton', 'Bridgetown', 'Cardiff', 'Mumbai', 'Adelaide', 'Tarouba', 'Birmingham', "St George's",
    'Kandy', 'Perth', 'Sharjah', 'Chittagong', 'Delhi', 'Ahmedabad', 'Providence', 'Brisbane', 'Chandigarh',
    'Kingston', 'Rajkot', 'Napier', 'Nagpur', 'Pune', 'Bangalore', 'Sylhet', 'Dambulla', 'Hobart', 'Trinidad'
])

# Sidebar - model info
st.sidebar.title("About the Model")
st.sidebar.info(
    """
    🎯 **T20 Score Predictor** uses a machine learning model (Random Forest Regressor) trained on historical T20 match data.
    
    📊 It considers:
    - Batting & bowling team
    - City
    - Current score
    - Overs completed
    - Wickets fallen
    - Last 5 overs' performance
    
    ⚡ Predicts the **final score** based on these features.
    """
)



# Title & logo
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏏 T20 World Cup Score Predictor 🏆</h1>", unsafe_allow_html=True)
st.markdown("---")

logo_col = st.columns([1, 2, 1])
with logo_col[1]:
    st.image("images/cricket_logo.png", width=150)

st.markdown("## Participating Teams", unsafe_allow_html=True)
st.markdown("---")

# Team logos (small)
team_logos = {
    "West Indies": "images/west_indies.png",
    "Australia": "images/australia.png",
    "Bangladesh": "images/bangladesh.png",
    "India": "images/india.png",
    "New Zealand": "images/new_zealand.png",
    "Pakistan": "images/pakistan.png",
    "South Africa": "images/southafrica.png",
    "Sri Lanka": "images/sri_lanka.png"
}

cols = st.columns(4)
for idx, (team, logo) in enumerate(team_logos.items()):
    with cols[idx % 4]:
        st.image(logo, caption=team, width=100)

st.markdown("---")
st.subheader("🏟️ Match Details")

# Match input form
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', cities)

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs Done (min 5)', min_value=5.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10, step=1)

last_five = st.number_input('Runs Scored in Last 5 Overs')

# Predict button
if st.button('Predict Score'):
    balls_left = 120 - int(overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'crr': [crr],
        'last_five': [last_five]
    })

    prediction = pipe.predict(input_df)[0]
    st.success(f"🎯 Predicted Final Score: {int(prediction)} Runs")

st.markdown("---")
st.markdown("<h4 style='text-align: center; color: gray;'>🏆 Powered by Machine Learning • Enjoy the Game!</h4>", unsafe_allow_html=True)
