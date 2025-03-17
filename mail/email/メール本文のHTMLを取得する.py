import email
from typing import Union


def get_body_html(mail: Union[email.message.EmailMessage, email.message.Message]) -> str:
    """メール本文のHTMLを取得する

    Parameters:
        mail (email.message.EmailMessage | email.message.Message)

    Returns:
        str: HTML。見つからなければ空文字列."""
    
    html_contents = []
    for part in mail.walk():
        # 添付ファイルをスキップ
        content_disposition = part.get("Content-Disposition")
        if content_disposition == "attachment":
            continue

        content_type = part.get_content_type()
        content_encoding = part.get_content_charset() or "utf-8"
        if content_type == "text/html":
            html_contents.append(part.get_payload(decode=True).decode(content_encoding, errors="replace"))

    if html_contents:
        return "\n".join(html_contents)
    else:
        return ""
