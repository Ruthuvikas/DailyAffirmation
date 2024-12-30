import smtplib
from email.mime.text import MIMEText
import random
import os

# Email credentials
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# List of affirmations
AFFIRMATIONS = [
    "You are worthy of love and respect.",
    "Every day is a fresh start.",
    "You have the power to create change.",
    "You are strong, capable, and resilient.",
]

def send_email(affirmation):
    """Send an email."""
    try:
        msg = MIMEText(affirmation)
        msg["Subject"] = "Your Daily Affirmation"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECIPIENT_EMAIL

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print("Email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    affirmation = random.choice(AFFIRMATIONS)
    send_email(affirmation)
