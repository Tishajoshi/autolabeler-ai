#Final polish for CertifyO Hackathon submission on June 29, 2025 🎯

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_issue(title, body):
    prompt = f"""
You are an AI assistant helping to label GitHub issues. Choose one label from this list:
[bug, enhancement, feature, question, documentation]

Issue Title: {title}
Issue Body: {body}

Label:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Classify GitHub issues by label."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip().lower()
