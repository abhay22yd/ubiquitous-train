import streamlit as st
from detect import detect_phishing

st.set_page_config(page_title="Phishing Detector", layout="centered")

st.image("static/logo.png", width=150)
st.title("🛡️ AI-Powered Phishing Detection")
st.write("Paste a suspicious email or message below, or upload a `.txt` file.")

# Text input
email_input = st.text_area("✉️ Email or Message Text", height=200)

# File upload
uploaded_file = st.file_uploader("📁 Or upload a .txt file", type=["txt"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    email_input = content
    st.text_area("📄 File Content", content, height=200)

# Analyze button
if st.button("🔍 Analyze"):
    if email_input.strip():
        label, score = detect_phishing(email_input)
        st.markdown(f"### ✅ Result: `{label}`")
        st.markdown(f"**Confidence Score:** `{score}%`")
        if label == "Phishing":
            st.error("⚠️ Warning: This message may be a phishing attempt.")
        else:
            st.success("✅ This message seems safe.")
    else:
        st.warning("Please enter or upload some text to analyze.")
