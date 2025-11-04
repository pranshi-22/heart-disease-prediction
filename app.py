import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

# App title
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color:#FF4B4B;'>❤️ Heart Disease Prediction App</h1>
        <h3 style='color:#1E90FF;'>Predict Your Heart Health Using Machine Learning</h3>
        <p style='font-size:16px;'>Built by <b>Pranshi</b> | Powered by Logistic Regression</p>
        <hr style='border:1px solid #FF4B4B;'>
    </div>
    """,
    unsafe_allow_html=True
)

# Input fields for user data
st.sidebar.header('Enter Patient Details')

age = st.sidebar.number_input('Age', 1, 120, 25)
sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
cp = st.sidebar.selectbox('Chest Pain Type (cp)', [0, 1, 2, 3])
trestbps = st.sidebar.number_input('Resting Blood Pressure (trestbps)', 80, 200, 120)
chol = st.sidebar.number_input('Serum Cholestoral (chol)', 100, 600, 200)
fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', [0, 1])
restecg = st.sidebar.selectbox('Resting ECG results (restecg)', [0, 1, 2])
thalach = st.sidebar.number_input('Maximum Heart Rate Achieved (thalach)', 60, 220, 150)
exang = st.sidebar.selectbox('Exercise Induced Angina (exang)', [0, 1])
oldpeak = st.sidebar.number_input('ST depression induced by exercise (oldpeak)', 0.0, 10.0, 1.0)
slope = st.sidebar.selectbox('Slope of the peak exercise ST segment (slope)', [0, 1, 2])
ca = st.sidebar.selectbox('Number of major vessels (ca)', [0, 1, 2, 3, 4])
thal = st.sidebar.selectbox('Thalassemia (thal)', [0, 1, 2, 3])

# Convert inputs into a DataFrame
user_input = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == 'Male' else 0],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

st.subheader('🧾 Entered Patient Data:')
st.write(user_input)

# Predict button
if st.button('🔍 Predict'):
    prediction = model.predict(user_input)[0]
    if prediction == 1:
        st.error('⚠️ The model predicts that this person **is likely to have Heart Disease.**')
    else:
        st.success('✅ The model predicts that this person **is unlikely to have Heart Disease.**')

st.markdown("---")
st.markdown("<p style='text-align:center;'>Developed by <b>Pranshi Sharma</b> 💖</p>", unsafe_allow_html=True)
