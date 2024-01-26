import random
import cv2
import numpy as np
import os
import pyautogui
import time
import keyboard

script_dir = os.path.dirname(os.path.abspath(__file__))


def find_image_on_screen(template_path, threshold=0.92):
    # Load the template image
    template = cv2.imread(template_path, 0)

    # Get the screen image
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Match the template with the screen image
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    # Get the coordinates of the matched region
    coordinates = list(zip(*locations[::-1]))

    # Calculate the center position of the bounding box
    centers = []
    for loc in coordinates:
        w, h = template.shape[::-1]
        center_x = loc[0] + w // 2
        center_y = loc[1] + h // 2
        centers.append((center_x, center_y))

    #return centers[1::2]
    return centers

def auto_click_on_centers(centers):
    for center in centers:
        # Move the mouse to the center position
        pyautogui.moveTo(center[0], center[1])

        # Click at the center position
        pyautogui.click()

        time.sleep(random.choice([0.15]))

# Example usage
# folder_path = 'C:\\Users\\ADMIN\\Desktop\\Python\\AutoAddFrsFb\\image'
# image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
image_path = os.path.join(script_dir, 'img\\ImgAddFrs\\add.png')

countNotFound = 0

def auto_click_add():

    global countNotFound  # Declare countNotFound as global

    centers = find_image_on_screen(image_path)

    if centers:
            print(f"Position: {centers}")
            auto_click_on_centers(centers)
    else:
            print(f"Image '1.png' not found.")
            countNotFound += 1
            print(countNotFound)
            if countNotFound > 8:
                keyboard.press_and_release('ctrl+w')
                time.sleep(1)
                countNotFound = 0



def detect_image(template_path, threshold=0.92):
    # Load the template image
    template = cv2.imread(template_path, 0)

    # Get the screen image
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Match the template with the screen image
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    # Get the coordinates of the first matched region
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
    # Example usage
    # template_path = 'C:\\Users\\ADMIN\\Desktop\\Python\\AutoAddFrsFb\\ok.png'
    template_path = os.path.join(script_dir, 'img\\ImgAddFrs\\ok.png')
    is_image_found, image_positions = detect_image(template_path)

    if is_image_found:
        print(f"OK Button: {image_positions}")
        pyautogui.moveTo(image_positions[0], image_positions[1])
        pyautogui.click()
        pyautogui.scroll(800)
        time.sleep(0.8)
        auto_click_add()
    else:
        print("No OK button!!!")
        pyautogui.scroll(800)
        time.sleep(0.8)
        auto_click_add()

def detect_x_btn():
    # Example usage
    # template_path = 'C:\\Users\\ADMIN\\Desktop\\Python\\AutoAddFrsFb\\2.png'
    template_path = os.path.join(script_dir, 'img\\ImgAddFrs\\closecall.png')
    is_image_found, image_positions = detect_image(template_path)

    if is_image_found:
        print(f"X Button: {image_positions}")
        pyautogui.moveTo(image_positions[0], image_positions[1])
        pyautogui.click()
 
    
while True:
    detect_ok_btn()
    detect_x_btn()
    time.sleep(2.2)
