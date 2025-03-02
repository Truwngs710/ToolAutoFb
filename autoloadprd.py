import pyautogui
import pandas as pd
import os
import time
import pyperclip

# Thiết lập FAILSAFE cho pyautogui
pyautogui.FAILSAFE = False

# Lưu trữ vị trí đã tìm thấy để tái sử dụng
found_positions = {}

def make_path(path):
    """Hàm tạo đường dẫn đầy đủ từ đường dẫn tương đối"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, path)

def find_and_click(image_path, confidence=0.96):
    """Hàm tìm và click vào hình ảnh trên màn hình"""
    global found_positions
    filename = os.path.basename(image_path)
    if filename in found_positions:
        pyautogui.click(found_positions[filename])
        print(f"Reused click {filename}")
        return True

    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            found_positions[filename] = location
            pyautogui.click(location)
            print(f"Click {filename}")
            return True
        else:
            print(f"Not found {filename}")
            return False
    except Exception as e:
        print(f"Error with {filename}: {e}")
        return False

def copy_to_clipboard(data):
    """Hàm copy dữ liệu vào clipboard và kiểm tra"""
    pyperclip.copy(data)
    time.sleep(0.5)
    if pyperclip.paste() != data:
        print("Failed to copy to clipboard")
        return False
    return True

def get_ordered_content(csv_file_path):
    """Hàm lấy dữ liệu từ file CSV theo thứ tự"""
    df = pd.read_csv(csv_file_path)
    return df.iloc[:, 0].tolist()  # Lấy cột đầu tiên

def is_duplicate(link, linkold_path):
    """Hàm kiểm tra xem link có tồn tại trong linkold.csv không"""
    df = pd.read_csv(linkold_path)
    return link in df.iloc[:, 0].tolist()

def update_csv_files(current_link, linknew_path, linkold_path):
    """Hàm cập nhật file CSV: xóa link hiện tại khỏi linknew.csv và thêm vào linkold.csv"""
    df_new = pd.read_csv(linknew_path)
    df_old = pd.read_csv(linkold_path)

    # Loại bỏ link khỏi linknew.csv
    df_new = df_new[df_new.iloc[:, 0] != current_link]
    df_new.to_csv(linknew_path, index=False)

    # Thêm link vào linkold.csv
    df_old.loc[len(df_old)] = [current_link]
    df_old.to_csv(linkold_path, index=False)

def wait_and_click(image_path, confidence=0.96, timeout=10):
    """Hàm chờ và click hình ảnh với thời gian timeout"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            print(f"Clicked on {os.path.basename(image_path)}")
            return True
        time.sleep(0.5)
    print(f"Timeout waiting for {os.path.basename(image_path)}")
    return False

def main_loop():
    """Vòng lặp chính của chương trình"""
    csv_file_path = make_path('csv/linknew.csv')
    old_csv_file_path = make_path('csv/linkold.csv')
    contents = get_ordered_content(csv_file_path)
    content_index = 0
    iteration = 0

    while content_index < len(contents):
        current_content = contents[content_index]

        # Kiểm tra trùng lặp
        if is_duplicate(current_content, old_csv_file_path):
            print(f"Duplicate found: {current_content}, removing from linknew.csv")
            update_csv_files(current_content, csv_file_path, old_csv_file_path)
            contents = get_ordered_content(csv_file_path)
            continue

        iteration += 1
        if not copy_to_clipboard(current_content):
            print(f"Failed to copy: {current_content}")
            continue

        print(f"[{iteration}] Copy link: {current_content}")

        # Thực hiện các hành động tự động hóa
        wait_and_click(make_path('img/autocty/newtab.png'))
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        print("Paste dữ liệu thành công.")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(9)
        wait_and_click(make_path('img/autocty/opencrawl.png'))
        time.sleep(3)
        wait_and_click(make_path('img/autocty/loadsp.png'))
        time.sleep(3)
        wait_and_click(make_path('img/autocty/cate.png'))
        time.sleep(3)
        wait_and_click(make_path('img/autocty/ts1.png'))
        time.sleep(3)
        pyautogui.scroll(-1200)
        time.sleep(2)
        wait_and_click(make_path('img/autocty/save.png'))
        time.sleep(8.5)
        pyautogui.hotkey('ctrl', 'w')
        print("Cào sản phẩm thành công.")
        time.sleep(3)

        # Cập nhật file CSV
        update_csv_files(current_content, csv_file_path, old_csv_file_path)

        # Chuyển sang link tiếp theo
        content_index += 1

    print("Đã xử lý hết tất cả nội dung trong file CSV.")

if __name__ == "__main__":
    main_loop()
