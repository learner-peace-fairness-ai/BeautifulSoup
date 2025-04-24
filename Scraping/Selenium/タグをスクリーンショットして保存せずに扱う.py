from io import BytesIO

from PIL import Image

バイナリ = タグ.screenshot_as_png
with BytesIO(バイナリ) as buf:
    with Image.open(buf) as img:
        img.load()
        処理
