# app.py

import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load and preprocess dataset
@st.cache_resource
def load_model():
    df = pd.read_csv("Phishing_Legitimate_full.csv")

    # Assuming the dataset has 'email' and 'label' columns
    X = df['email']
    y = df['label']

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save model and vectorizer
    joblib.dump(model, 'phishing_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    return model, vectorizer

# Load model and vectorizer
model, vectorizer = load_model()

# Streamlit app interface
st.title("📧 AI Phishing Email Detection")
st.write("Enter an email message below to check if it's phishing or legitimate.")

email_input = st.text_area("Email content", height=200)

if st.button("Predict"):
    if email_input.strip() == "":
        st.warning("Please enter email text.")
    else:
        input_vector = vectorizer.transform([email_input])
        prediction = model.predict(input_vector)[0]
        result = "🔒 Legitimate Email" if prediction == 0 else "⚠️ Phishing Email"
        st.success(f"Prediction: {result}")
