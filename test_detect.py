from detect import detect_phishing

# Test messages
messages = [
    "Dear user, your account has been suspended. Click here to verify your login details.",
    "Hey, just checking in to see how you’re doing. Let's catch up soon!",
    "Urgent! Update your bank password now to avoid suspension.",
    "We’re hosting a team lunch tomorrow at 1 PM. Don’t miss it!"
]

# Run detection on each message
for i, msg in enumerate(messages):
    label, score = detect_phishing(msg)
    print(f"\nMessage {i+1}: {msg}")
    print(f"→ Result: {label} | Confidence: {score}%")