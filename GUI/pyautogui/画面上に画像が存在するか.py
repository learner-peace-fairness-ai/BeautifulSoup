# ※ OpenCVをインストールしておく必要がある
def exists_image_on_screen(image_path, confidence: float = 0.9):
    locations = list(pyautogui.locateAllOnScreen(image_path, confidence=confidence))
    if locations:
        return True
    else:
        return False
