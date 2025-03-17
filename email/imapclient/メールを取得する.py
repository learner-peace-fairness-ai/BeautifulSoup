import email
from email.parser import BytesParser
from typing import Union

import imapclient


def get_mail(client: imapclient.IMAPClient, mail_id: str) -> (Union[email.message.EmailMessage, email.message.Message]):
    """指定したIDのメールオブジェクトを取得する

    Parameters:
        client (imapclient.IMAPClient)
        mail_id (str): メールID.

    Returns:
        email.message.EmailMessage | email.message.Message: メールオブジェクト."""
    
    raw_message = client.fetch(mail_id, ['BODY[]'])
    raw_email = raw_message[mail_id][b'BODY[]']
    return BytesParser().parsebytes(raw_email)
