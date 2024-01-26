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
        # Locate the center coordinates of the image on the screen
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)

        # Click the center of the image
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
        # Open the CSV file with the specified encoding
        with open(csv_file_path, 'r', encoding=csv_encoding) as file:
            # Create a CSV DictReader
            csv_reader = csv.DictReader(file)

            # Check if the target column exists in the CSV file
            if target_column_name not in csv_reader.fieldnames:
                print(f"Column '{target_column_name}' not found in the CSV file.")
                return None
            else:
                # Collect all 'content' values into a list
                content_values = [row[target_column_name] for row in csv_reader]

                # Check if there are values in the list
                if content_values:
                    # Choose a random 'content' value
                    random_content = random.choice(content_values)
                    return random_content
                else:
                    print("No 'content' values found in the CSV file.")
                    return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
iteration = 1  # Counter for iterations

# Step 3: Detect and Click 'cmt.png'
while True:
    
    find_and_click(make_path('img\\ImgCmtReel\\close.png'))
    time.sleep(1)
    find_and_click(make_path('img\\ImgCmtReel\\closecall.png'))
    time.sleep(1)
    find_and_click(make_path('img\\ImgCmtReel\\like.png'))
    time.sleep(1)
    if find_and_click(make_path('img\\ImgCmtReel\\cmt.png')):
        time.sleep(3)  # Add a delay for the page to load, adjust as needed

        # Step 4: Choose random content from CSV file
        random_content = get_random_content_value(make_path('csv\\Thuong - link aff.csv'))
        pyperclip.copy(random_content)
        time.sleep(3)
        if random_content:
            # Step 5: Paste the random content and press Enter
            pyautogui.hotkey('ctrl', 'v')
            print('paste data')
            time.sleep(8)
            pyautogui.press('enter')
            time.sleep(12)  # Add a delay for the page to process the input, adjust as needed

            # Step 6: Detect and Click 'next.png'
            find_and_click(make_path('img\\ImgCmtReel\\next.png'))
            time.sleep(3)
            print(f"Iteration: {iteration}")
            iteration += 1
            if iteration >= 6: 
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
        
        find_and_click(make_path('img\\ImgCmtReel\\next.png'))
        time.sleep(3)
