# ※ OpenCVをインストールしておく必要がある
def exists_image_on_screen(image_path, confidence: float = 0.9):
    try:
        pyautogui.locateOnScreen(image_path, confidence=confidence)
        return True
    except:
        return False
