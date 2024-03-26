import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach message body
    msg.attach(MIMEText(message, "plain"))

    # Send email
    smtp_server.send_message(msg)

    # Close connection
    smtp_server.quit()


# Example usage
sender_email = ""
sender_password = ""
recipient_email = ""
subject = "Wywóz śmieci"
message = "Śmieci są do wyjebania"

send_email(sender_email, sender_password, recipient_email, subject, message)
