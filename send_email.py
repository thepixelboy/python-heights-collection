import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


def send_email(email_address, height, average_height, population):
    """This function sends an email to the user, with height statistics"""
    smtp_server = os.getenv("MAILJET_SMTP")
    smtp_username = os.getenv("MAILJET_USERNAME")
    smtp_password = os.getenv("MAILJET_PASSWORD")

    from_email = email_address
    to_email = email_address
    subject = "Height data statistics"
    message = f"Hey there, your height is <strong>{height}cm</strong>.\nThe average height for the entire population of {population} people stored in the database is <strong>{average_height}cm</strong>."

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP(smtp_server, 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(smtp_username, smtp_password)
    gmail.send_message(msg)
