import smtplib
from email.mime.text import MIMEText
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Email credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Initialize GPT model
model = ChatOpenAI(temperature=0.7, model_name="gpt-4")

# System prompt for generating affirmations
system_prompt = """You are a Daily Affirmation generator. Generate unique, motivational affirmations with emojis. Each affirmation should be derived from Bhagavad Gita."""

def generate_affirmation():
    """Generate a daily affirmation using GPT."""
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content="Generate a motivational daily affirmation.")
        ]
        response = model(messages)
        return response.content.strip()
    except Exception as e:
        print(f"Failed to generate affirmation: {e}")
        return "You are capable of achieving greatness! 🌟"

def send_email(affirmation):
    """Send an email with the generated affirmation."""
    try:
        msg = MIMEText(affirmation)
        msg["Subject"] = "Your Daily Affirmation \U0001FA77"
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
    # Generate affirmation using GPT
    affirmation = generate_affirmation()
    print(f"Generated Affirmation: {affirmation}")

    # Send the affirmation via email
    send_email(affirmation)
