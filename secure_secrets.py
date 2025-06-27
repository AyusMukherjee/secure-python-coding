from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file

DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")

def connect_db():
    print("Connecting with password: [REDACTED]")

connect_db()