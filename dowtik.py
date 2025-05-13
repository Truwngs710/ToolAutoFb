import pyautogui
import cv2
import time
import csv
import os
import random
import pyperclip


script_dir = os.path.dirname(os.path.abspath(__file__))
def make_path(path):
    return os.path.join(script_dir, path)

def find_and_click(image_path, confidence=0.97):
    filename = image_path.split('\\')[-1]
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            print("click {}".format(filename))
            return True
        else:
            print("Notfound {}".format(filename))
            return False
    except Exception as e:
        print("Not found {}".format(filename))
        return False
    
while True:
    # lấy URL
    find_and_click(make_path('img\\downtik\\link.png'))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # Chuyển tới tab download
    find_and_click(make_path('img\\downtik\\webdown.png'))
    time.sleep(1)

    # Nhập URL và tải video
    find_and_click(make_path('img\\downtik\\pastelink.png'))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    find_and_click(make_path('img\\downtik\\down1.png'))
    time.sleep(3)
    find_and_click(make_path('img\\downtik\\down2.png'))
    time.sleep(1)
    find_and_click(make_path('img\\downtik\\out1.png'))
    time.sleep(1)
    # Load lại trang tải
    find_and_click(make_path('img\\downtik\\out2.png'))
    time.sleep(1)
    # Chuyển tới tab Reel
    find_and_click(make_path('img\\downtik\\tik.png'))
    time.sleep(1)
    pyautogui.click(x=500, y=500)
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)


