import numpy as np
import time
import mss
import pyautogui

print("Switch to Dino game...")
time.sleep(5)
print("Ready")

SCAN_REGION = {
    "left": 140      ,
    "top": 590 ,
    "width": 110,
    "height": 80
}
pyautogui.press("space")
last_jump = 0
prev_detect = False

with mss.mss() as sct:
    while True:
        try:
            screenshot = sct.grab(SCAN_REGION)
        except:
            continue

        img = np.array(screenshot)

        gray = np.mean(img[:, :, :3], axis=2)
        gray = gray[:-20, :]
        front = gray[:int(gray.shape[0]*0.7), :40]

        cols = np.sum(front < 120, axis=0)
        cols = np.convolve(cols, np.ones(3), mode='same')

        distance = None
        for i, val in enumerate(cols):
            print(val)
            if val > 5:
                distance = i

                break

        threshold = 10

        detected = distance is not None and distance < threshold

        if detected and prev_detect and time.time() - last_jump > 0.15:
            pyautogui.press("space")
            print("Jump")
            last_jump = time.time()

        prev_detect = detected

