import streamlit as st

# Placeholder for the phishing email detection model
# Replace with your actual model loading and prediction function
def phishing_email_detection(email_content):
    # Sample placeholder logic for testing, replace with your model
    if "suspicious" in email_content or "click here" in email_content:
        return "Phishing"
    else:
        return "Legitimate"

# Streamlit layout
st.title('Phishing Email Detection')

# Create a box structure where user can input emails
email_content = st.text_area("Enter Email Content", height=200)

# Buttons for "Check" and "Stop"
if st.button('Check'):
    if email_content:
        prediction = phishing_email_detection(email_content)
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Please enter some email content.")

if st.button('Stop'):
    st.write("Email Check Stopped.")
    email_content = ""  # Reset email content
    st.text_area("Enter Email Content", height=200, value=email_content)
