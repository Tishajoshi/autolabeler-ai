# labeler.py

def classify_issue(title, body):
    print("⚠️ Using fallback classifier (no OpenAI API)")

    # Naive rule-based classifier for demo/hackathon testing
    text = (title + " " + body).lower()

    if "error" in text or "not working" in text or "fail" in text:
        return "bug"
    elif "add" in text or "feature" in text or "support" in text:
        return "enhancement"
    elif "how" in text or "what" in text or "why" in text or "can i" in text:
        return "question"
    else:
        return "discussion"
