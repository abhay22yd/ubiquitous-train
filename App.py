import streamlit as st
from detect import detect_phishing

st.set_page_config(page_title="Phishing Detector", layout="centered")

st.title("🛡 AI-Powered Phishing Detection")
st.write("Paste a suspicious email or message below to analyze its risk level.")

# Text input box
email_input = st.text_area("✉ Email or Message Text", height=200)

# Analyze button
if st.button("🔍 Analyze"):
    if email_input.strip():
        label, score = detect_phishing(email_input)
        st.markdown(f"### ✅ Result: {label}")
        st.markdown(f"*Confidence Score:* {score}%")
        if label == "Phishing":
            st.error("⚠ Warning: This message may be a phishing attempt.")
        else:
            st.success("✅ This message seems safe.")
    else:
        st.warning("Please enter some text to analyze.")