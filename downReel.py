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
    
    # next reel
    time.sleep(1)
    pyautogui.click(x=1500, y=500)
    time.sleep(2)

    # lấy URL
    find_and_click(make_path('img\\downreel\\link.png'))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # Chuyển tới tab download
    find_and_click(make_path('img\\downreel\\downloadweb.png'))
    time.sleep(1)

    # Nhập URL và tải video
    find_and_click(make_path('img\\downreel\\input.png'))
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    find_and_click(make_path('img\\downreel\\download.png'))
    time.sleep(6)
    find_and_click(make_path('img\\downreel\\dow.png'))
    time.sleep(1)
    find_and_click(make_path('img\\downreel\\closeads.png'))
    time.sleep(1)
    # Load lại trang tải
    find_and_click(make_path('img\\downreel\\reload.png'))
    time.sleep(1)
    # Chuyển tới tab Reel
    find_and_click(make_path('img\\downreel\\fb.png'))
    time.sleep(1)

