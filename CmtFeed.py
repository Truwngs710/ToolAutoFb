import pyautogui
import cv2
import time
import csv
import os
import random
import pyperclip

global count
script_dir = os.path.dirname(os.path.abspath(__file__))

def make_path(path):
    return os.path.join(script_dir, path)

def find_and_click(image_path, confidence=0.90):
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

def get_random_content_value(csv_file_path, target_column_name='content', csv_encoding='utf-8'):
    try:
        with open(csv_file_path, 'r', encoding=csv_encoding) as file:
            csv_reader = csv.DictReader(file)
            if target_column_name not in csv_reader.fieldnames:
                print(f"Column '{target_column_name}' not found in the CSV file.")
                return None
            else:
                content_values = [row[target_column_name] for row in csv_reader]
                if content_values:
                    random_content = random.choice(content_values)
                    return random_content
                else:
                    print("No 'content' values found in the CSV file.")
                    return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
iteration = 1  

while True:
    find_and_click(make_path('img\\ImgCmtFeed\\closecall.png'))
    time.sleep(1)
    find_and_click(make_path('img\\ImgCmtFeed\\ok.png'))
    time.sleep(1)
    find_and_click(make_path('img\\ImgCmtFeed\\closemes.png'))
    time.sleep(1)
    pyautogui.scroll(-2000)
    time.sleep(2)
    find_and_click(make_path('img\\ImgCmtFeed\\cmt.png'))
    time.sleep(6)
    if find_and_click(make_path('img\\ImgCmtFeed\\writecmt.png')):
        time.sleep(3) 
        random_content = get_random_content_value(make_path('csv\\Thuong - link aff.csv'))
        pyperclip.copy(random_content)
        time.sleep(3)
        if random_content:
            pyautogui.hotkey('ctrl', 'v')
            print('paste data')
            time.sleep(6)
            pyautogui.press('enter')
            time.sleep(8)
            find_and_click(make_path('img\\ImgCmtFeed\\closepost.png'))
            time.sleep(3)
            print(f"Iteration: {iteration}")
            iteration += 1
            if iteration >= 3: 
                pyautogui.keyDown('alt')
                time.sleep(0.5)
                for _ in range(3):
                    pyautogui.press('tab')
                    time.sleep(0.5)
                pyautogui.keyUp('alt')
                time.sleep(0.5)
                iteration = 1 

        else:
            print("Skipping typing and pressing Enter as no random content is available.")
    else:
        find_and_click(make_path('img\\ImgCmtFeed\\closepost.png'))
        time.sleep(2)
        pyautogui.scroll(-2000)
        time.sleep(3)
        

