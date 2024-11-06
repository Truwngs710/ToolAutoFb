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

def get_random_content_value(csv_file_path, target_column_name='A', csv_encoding='utf-8'):
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
    iteration = iteration+1
    random_number = random.randint(1, 3)
    print(random_number)

    if random_number == 2:
        find_and_click(make_path('img\\ImgCmtFeed\\closecall.png'))
        time.sleep(1)
        find_and_click(make_path('img\\ImgCmtFeed\\ok.png'))
        time.sleep(1)
        find_and_click(make_path('img\\ImgCmtFeed\\like.png'))
        time.sleep(2)
        find_and_click(make_path('img\\ImgCmtFeed\\incmt.png'))
        time.sleep(7)
        random_content = get_random_content_value(make_path('csv\\data.csv'))
        pyperclip.copy(random_content)
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'v')
        print('paste data')
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(4)
        find_and_click(make_path('img\\ImgCmtFeed\\clspost.png'))
        time.sleep(5)
        
    pyautogui.scroll(-2000)
    time.sleep(2)
    if iteration == 100: 
        pyautogui.keyDown('alt')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.keyUp('alt')
        iteration= 1

