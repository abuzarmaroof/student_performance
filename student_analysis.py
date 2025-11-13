import streamlit as st
import pickle
import numpy as np

with open('student_perfomence.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Student Performance Prediction System")
st.markdown("Enter student academic and lifestyle details to predict performance.")
st.markdown("---")

st.subheader("Enter Student Details")

# Inputs
hours_studied = st.number_input("Hours Studied per Day", min_value=0, max_value=10)
previous_scores = st.number_input("Previous Exam Score", min_value=0, max_value=100)
extracurricular = st.radio("Participates in Extracurricular Activities", ["Yes", "No"])
sleep_hours = st.number_input("Average Sleep Hours per Day", min_value=0, max_value=24)
sample_papers = st.number_input("Number of Sample Question Papers Practiced", min_value=0, max_value=50)

# Encoding categorical
if extracurricular == "Yes":
    extracurricular = 1
else:
    extracurricular = 0

st.markdown("---")

# Prediction
if st.button("Predict Performance"):
    features = np.array([[hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers]])
    prediction = model.predict(features)
    prediction=int(prediction)
    st.success(f"Predicted Performance: {prediction}")