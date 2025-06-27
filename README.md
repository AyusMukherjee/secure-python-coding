# secure-python-coding

![Security Shield](https://img.shields.io/badge/Security-Level_Orange-red) 
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)

A demonstration of common security vulnerabilities in Python and their secure counterparts, with comparative analysis.

## 🚀 Features

- SQL Injection vulnerable/safe implementations
- Hardcoded secrets vs environment variables
- Dangerous deserialization vs safe JSON
- Security comparison: Python vs Java
- Bandit static analysis integration

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AyusMukherjee/secure-python-coding.git
   cd secure-python-demo
2. Set up virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows

3. Install dependencies:
   bash
   pip install -r requirements.txt

🛠️ How to Run
🔓 Insecure Examples

# SQL Injection vulnerable app
python insecure_app.py

# Hardcoded secrets demo
python insecure_secrets.py

# Dangerous deserialization (WARNING: Executes shell commands)
python insecure_pickle.py

🔒 Secure Examples

# Parameterized queries app
python secure_app.py

# Environment variables demo
python secure_secrets.py

# Safe serialization
python secure_serialization.py


# Codes for visulizations:
https://colab.research.google.com/drive/1nzcFHko3ygHShIiIwrgxYTjoU9Rh2upa?usp=sharing
