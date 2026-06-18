import sqlite3
import smtplib
from email.message import EmailMessage

from email_config import (
    SENDER_EMAIL,
    SENDER_PASSWORD,
    RECEIVER_EMAIL
)

# Connect to database
conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

# Get top opportunity projects
cursor.execute("""
SELECT
    project_name,
    opportunity_score
FROM projects
WHERE opportunity_score >= 70
ORDER BY opportunity_score DESC
LIMIT 5
""")

projects = cursor.fetchall()

conn.close()

if not projects:
    print("No high opportunity projects found.")

else:

    body = """
Infrastructure Intelligence Alert

Top High-Opportunity Projects

"""

    for project, score in projects:

        body += (
            f"Project: {project}\n"
            f"Opportunity Score: {score}\n\n"
        )

    msg = EmailMessage()

    msg["Subject"] = "🚨 Infrastructure Opportunity Alert"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    msg.set_content(body)

    try:

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                SENDER_EMAIL,
                SENDER_PASSWORD
            )

            smtp.send_message(msg)

        print("✅ Email alert sent successfully!")

    except Exception as e:

        print(f"❌ Error sending email: {e}")