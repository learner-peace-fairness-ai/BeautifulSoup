import email
from typing import Union


def get_email_body_text(mail: Union[email.message.EmailMessage, email.message.Message]):
    """メール本文のテキストを取得する

    Parameters:
        mail (email.message.EmailMessage | email.message.Message)

    Returns:
        str: テキスト。見つからなければ空文字列."""
    
    text_contents = []
    for part in mail.walk():
        # 添付ファイルをスキップ
        content_disposition = part.get("Content-Disposition")
        if content_disposition == "attachment":
            continue

        content_type = part.get_content_type()
        content_encoding = part.get_content_charset() or "utf-8"
        if content_type == "text/plain":
            text_contents.append(part.get_payload(decode=True).decode(content_encoding, errors="replace"))

    if text_contents:
        return "\n".join(text_contents)
    else:
        return ""
