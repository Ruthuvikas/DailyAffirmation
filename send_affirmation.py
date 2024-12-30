import smtplib
from email.mime.text import MIMEText
import random

# Email credentials
SENDER_EMAIL = "ruthuvikas.28@gmail.com"
SENDER_PASSWORD = "exlw xhii bphs srrd"
RECIPIENT_EMAIL = "rvravikumar@ucdavis.edu"

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
