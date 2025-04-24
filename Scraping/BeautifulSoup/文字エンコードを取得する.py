def get_encoding(soup):
    """<meta>から文字エンコードを取得する

    下記の順で文字エンコードを探す

    <meta charset="文字コード">
    <meta http-equiv="Content-Type" content="text/html; charset=文字コード">
    
    見つからなければ空文字列を返す.

    Parameters:
        soup (bs4.BeautifulSoup)

    Returns:
        str: 文字エンコード。見つからなければ空文字列."""
    
    # <meta charset="文字コード">
    meta_charset = soup.select_one("meta[charset]")
    if meta_charset:
        return meta_charset.get("charset")

    # <meta http-equiv="Content-Type" content="text/html; charset=文字コード">
    meta_content = soup.select_one("meta[http-equiv='Content-Type']")
    if not meta_content:
        return ""
    
    content = meta_content.get("content", "").lower()
    if "charset=" in content:
        return content.split("charset=")[-1]
    else:
        return ""
