import email
from email.header import decode_header
from typing import Union


def get_subject(mail: Union[email.message.EmailMessage, email.message.Message]):
    """メールのタイトルを取得する

    Parameters:
        mail (email.message.EmailMessage | email.message.Message)

    Returns:
        str: タイトル."""
    
    subject, encoding = decode_header(mail["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")
    return subject
