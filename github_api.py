import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("REPO_OWNER")
REPO = os.getenv("REPO_NAME")
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_issues():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def apply_label(issue_number, label):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue_number}/labels"
    response = requests.post(url, json={"labels": [label]}, headers=HEADERS)
    return response.status_code
