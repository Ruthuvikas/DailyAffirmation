# DailyAffirmation

DailyAffirmation is a Python-based project that sends motivational daily affirmations via email using OpenAI's GPT to generate unique affirmations.

---

## Features
- Automatically generates motivational affirmations daily using OpenAI GPT.
- Sends affirmations via email to a predefined recipient.
- Easy to deploy and schedule using GitHub Actions.

---

## Prerequisites
Before setting up the project, ensure you have:
- A [Gmail account](https://mail.google.com/) with an **App Password** configured for SMTP (if using Gmail).
- An [OpenAI API key](https://platform.openai.com/).
- Python 3.9 or later installed locally (for local testing).

---

## Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/yourusername/DailyAffirmation.git
cd DailyAffirmation
```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set Up Environment Variables
   ```bash
   SENDER_EMAIL=your_email@gmail.com
    SENDER_PASSWORD=your_app_password
    RECIPIENT_EMAIL=recipient_email@gmail.com
    OPENAI_API_KEY=your_openai_api_key
   ```
4. Test Locally
  ```bash
   python3 send_affirmation.py
   ```
### Deploy to Github Actions

Add Repository Secrets:

Go to Settings > Secrets and variables > Actions.
Add the following secrets:
SENDER_EMAIL
SENDER_PASSWORD
RECIPIENT_EMAIL
OPENAI_API_KEY
Workflow Schedule:

The GitHub Actions workflow (.github/workflows/daily_affirmation.yml) is configured to:
Generate a daily affirmation using OpenAI GPT.
Send the affirmation via email at 6:30 AM UTC.
Allow manual triggering of the workflow.
Run the Workflow:

The workflow will run daily as per the schedule.
To test the workflow manually, go to the Actions tab in your GitHub repository and trigger the workflow.

###Contribution
Feel free to fork this repository, make enhancements, and create pull requests. Contributions are always welcome!

###License
This project is licensed under the MIT License.




