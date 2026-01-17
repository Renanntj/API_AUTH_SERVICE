import smtplib
from email.message import EmailMessage
import secrets
from datetime import datetime, timedelta
from config import EMAIL, PASSWORD_APP, CODE_EXP


def generate_code() -> str:
    return f"{secrets.randbelow(10000):04}"


def generate_expiration(minutes: int = CODE_EXP):
    return datetime.now() + timedelta(minutes=minutes)


def send_email(to_email: str):
    code_hash = generate_code()
    expires_at = generate_expiration()

    if not EMAIL or not PASSWORD_APP:
        raise RuntimeError("Email credentials not configured")

    msg = EmailMessage()
    msg["Subject"] = "API AUTH SERVICE TEST"
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg.set_content(
        f"""This email is for portfolio testing purposes only.
To contact me, please visit my portfolio:
https://renanntj.github.io/Renan-Alves/

Your verification code is: {code_hash}
This code is valid for {CODE_EXP} minutes.
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD_APP)
        smtp.send_message(msg)

    return code_hash, expires_at


def validate_code(input_code: str, stored_code: str, expires_at: datetime) -> bool:
    if datetime.now() > expires_at:
        return False
    return input_code == stored_code
