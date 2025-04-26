from transformers import pipeline

# Create a simple text classification pipeline using a pre-trained BERT model
classifier = pipeline("text-classification", model="bert-base-uncased", top_k=1)

def detect_phishing(text):
    """
    Simulates phishing detection based on keywords + AI confidence.
    """
    # List of basic phishing trigger keywords (you can extend this list)
    phishing_keywords = ["password", "bank", "verify", "click here", "urgent", "account", "reset", "confirm", "login", "security alert"]

    # Check if any phishing keyword is in the text
    if any(keyword in text.lower() for keyword in phishing_keywords):
        label = "Phishing"
    else:
        label = "Safe"

    # Use the classifier to get a confidence score (using sentiment model as a stand-in)
    result = classifier(text)
# Get the first label from the result (depends on version)
    if isinstance(result, list) and isinstance(result[0], list):
        score = result[0][0]["score"]
    elif isinstance(result, list):
        score = result[0]["score"]
    else:
        score = 0.0  # fallback
    confidence = round(score * 100, 2)

    return label, confidence
