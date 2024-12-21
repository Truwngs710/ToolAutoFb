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

def find_and_click(image_path, confidence=0.96):
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
    find_and_click(make_path('img\\downreel\\next.png'))
    time.sleep(2)

    # lấy URL
    find_and_click(make_path('img\\downreel\\link.png'))
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    # Chuyển tới tab download
    find_and_click(make_path('img\\downreel\\downloadweb.png'))
    time.sleep(2)

    # Nhập URL và tải video
    find_and_click(make_path('img\\downreel\\input.png'))
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

    find_and_click(make_path('img\\downreel\\download.png'))
    time.sleep(5)
    find_and_click(make_path('img\\downreel\\dow.png'))
    time.sleep(3)
    # Load lại trang tải
    find_and_click(make_path('img\\downreel\\reload.png'))
    time.sleep(3)
    # Chuyển tới tab Reel
    find_and_click(make_path('img\\downreel\\fb.png'))
    time.sleep(3)

