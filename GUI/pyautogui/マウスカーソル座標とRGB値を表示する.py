# マウスカーソル座標とRGB値を表示する

import pyautogui

print('中断するにはCtrl-Cを押してください。')

try:
    while True:
        # マウス座標
        x, y = pyautogui.position()
        position_str = f'X: {x:>4} Y: {y:>4}'

        # RGB値
        with pyautogui.screenshot() as img:
            pixel_color = img.getpixel((x, y))
        position_str += f' RGB: ({pixel_color[0]:>3}, {pixel_color[1]:>3}, {pixel_color[2]:>3})'

        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\n終了。')
