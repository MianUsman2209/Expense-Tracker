import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAILS_FROM_EMAIL
from app.models.user import User

def send_email(to_email: str, subject: str, html_content: str):
    """
    Sends an email using the configured SMTP server.
    """
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        print(f"SMTP credentials not set. Scip sending email to {to_email}")
        print(f"Subject: {subject}")
        print(f"Content: {html_content}")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAILS_FROM_EMAIL or SMTP_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(html_content, 'html'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_otp_email(to_email: str, otp_code: str):
    """
    Sends an OTP email to the user.
    """
    subject = "Your Login OTP"
    html_content = f"""
    <html>
        <body>
            <h2>Login Verification</h2>
            <p>Your One-Time Password (OTP) is: <strong>{otp_code}</strong></p>
            <p>This code will expire in 10 minutes.</p>
        </body>
    </html>
    """
    send_email(to_email, subject, html_content)
