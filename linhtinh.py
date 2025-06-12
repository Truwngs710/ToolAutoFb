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
    
    time.sleep(3)
    find_and_click(make_path('img\\linhtinh\\galery.png'))
    time.sleep(1)
    find_and_click(make_path('img\\linhtinh\\galery.png'))
    time.sleep(3)
    
    pyautogui.click(x=1450, y=200)
    time.sleep(180)

    