import datetime
import logging
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

log = logging.getLogger("rotatingFileLogger")

# Email constants
mail_host: str = "smtp.sina.com"
mail_user: str = "johnnys_rpi_3b"
authorization_password: str = "dcbc7bdd4cb11187"
sender: str = f"{mail_user}@sina.com"
receivers: List[str] = ["johnnysviva@outlook.com"]


def build_message(receiver: str) -> MIMEMultipart:
    content: MIMEText = MIMEText(
        "This is a email from Python "
        + datetime.datetime.now().strftime("%Y-%m-%d %T"),
        "plain",
        "utf-8",
    )
    message: MIMEMultipart = MIMEMultipart()
    message["Subject"] = Header(
        "Emergency Security Alert, at "
        + datetime.datetime.now().strftime("%Y-%m-%d %T"),
        "utf-8",
    )
    message["From"] = Header(sender)
    message["To"] = Header(receiver)
    message["Cc"] = Header(sender)
    message.attach(content)
    return message


def send_email():
    smtp: smtplib.SMTP = smtplib.SMTP(mail_host, 25)
    smtp.connect(mail_host, 25)
    smtp.login(mail_user, authorization_password)
    for receiver in receivers:
        message: MIMEMultipart = build_message(receiver)
        try:
            log.info(f"Sending email. receiver: {receiver}")
            smtp.sendmail(sender, [receiver], message.as_string())
            log.info(
                f"Sent email successfully. {smtp}. receiver: {receiver}, message: {message}"
            )
        except smtplib.SMTPException:
            log.exception("Exception occurred while sending email!")
    smtp.quit()
