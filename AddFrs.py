import random
import cv2
import numpy as np
import os
import pyautogui
import time
import keyboard

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'img\\ImgAddFrs\\add.png')
countNotFound = 0

def find_image_on_screen(template_path, threshold=0.95):
    template = cv2.imread(template_path, 0)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    coordinates = list(zip(*locations[::-1]))
    centers = []
    for loc in coordinates:
        w, h = template.shape[::-1]
        center_x = loc[0] + w // 2
        center_y = loc[1] + h // 2
        centers.append((center_x, center_y))
    return centers

def auto_click_on_centers(centers):
    for center in centers:
        pyautogui.moveTo(center[0], center[1])
        pyautogui.click()
        time.sleep(random.choice([0.25, 0.5]))
        detect_ok_btn()
        detect_x_btn()
        time.sleep(1)
    pyautogui.scroll(800)
    

def auto_click_add():
    centers = find_image_on_screen(image_path)
    if centers:
            print(f"Position: {centers}")
            auto_click_on_centers(centers)
    else:
            print(f"Image '1.png' not found.")
            

def detect_image(template_path, threshold=0.95):
    template = cv2.imread(template_path, 0)
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    if len(locations[0]) > 0:
        x, y = locations[1][0], locations[0][0]
        center_x = x + template.shape[1] // 2
        center_y = y + template.shape[0] // 2
        center_position = (center_x, center_y)
        is_image_found = True
    else:
        center_position = None
        is_image_found = False
    return is_image_found, center_position

def detect_ok_btn():
    template_path = os.path.join(script_dir, 'img\\ImgAddFrs\\ok.png')
    is_image_found, image_positions = detect_image(template_path)
    if is_image_found:
        print(f"OK Button: {image_positions}")
        pyautogui.moveTo(image_positions[0], image_positions[1])
        pyautogui.click()
        time.sleep(1)
  

def detect_x_btn():
    template_path = os.path.join(script_dir, 'img\\ImgAddFrs\\closecall.png')
    is_image_found, image_positions = detect_image(template_path)
    if is_image_found:
        print(f"X Button: {image_positions}")
        pyautogui.moveTo(image_positions[0], image_positions[1])
        pyautogui.click()
        time.sleep(1)
    
while True:
    auto_click_add()
