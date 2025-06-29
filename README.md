# 🤖 AutoLabeler AI

![GitHub stars](https://img.shields.io/github/stars/Tishajoshi/autolabeler-ai?style=social)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)

AutoLabeler AI is an open-source Python tool that uses OpenAI’s GPT model to automatically label GitHub issues as `bug`, `feature`, `question`, `enhancement`, or `documentation`.

No more manually tagging dozens of issues — let the AI triage them for you! 🧠✨

📅 Final submission made on June 29, 2025, for the CertifyO Hackathon.

🧑‍💻 Solo project by Tisha Joshi

---

## 🚀 Features

- 🔎 Uses GPT-3.5 to analyze issue title + body
- 🏷️ Applies smart labels (`bug`, `feature`, `enhancement`, etc.)
- 🐙 Works on any GitHub repo (public or private)
- ✅ Fast setup using `.env` config file
- 💥 Includes fallback logic when OpenAI API quota is exceeded

---

## 🛠️ Tech Stack

- 🐍 Python 3.x
- 🧠 OpenAI GPT-3.5 API
- 🧪 GitHub REST API
- 🗂 `python-dotenv` for environment variables
- 📦 `requests` for API calls

---

## ⚙️ Setup Instructions

### 1. Clone this Repo

```bash
git clone https://github.com/Tishajoshi/autolabeler-ai.git
cd autolabeler-ai
