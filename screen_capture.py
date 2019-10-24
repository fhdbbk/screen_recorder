import numpy as np
import cv2
import pyautogui
# from PIL import ImageGrab
from PIL import Image

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

X_POS = 20
Y_POS = 20

mouse_pointer = Image.open('images/cursor.png')


def capture_screen():
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('../output.mp4', fourcc, 30.0, (SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Capturing the screen")
    while True:
        #img = ImageGrab.grab(bbox=(X_POS, Y_POS, SCREEN_WIDTH + X_POS, SCREEN_HEIGHT + Y_POS))
        img = pyautogui.screenshot(region=(X_POS, Y_POS, SCREEN_WIDTH, SCREEN_HEIGHT))
        x, y = pyautogui.position()
        img.paste(mouse_pointer, box=(x-20, y-20), mask=mouse_pointer)
        img_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(img_np)
        cv2.imshow("Screen", img_np)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    out.release()
    print("Released video")
    cv2.destroyAllWindows()
