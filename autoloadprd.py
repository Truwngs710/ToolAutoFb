import pyautogui
import csv
import os
import random
import time
import pyperclip

def make_path(path):
    """Hàm tạo đường dẫn đầy đủ từ đường dẫn tương đối"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, path)

def find_and_click(image_path, confidence=0.96):
    """Hàm tìm và click vào hình ảnh trên màn hình"""
    filename = os.path.basename(image_path)
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            print(f"Click {filename}")
            return True
        else:
            print(f"Not found {filename}")
            return False
    except Exception as e:
        print(f"Error with {filename}: {e}")
        return False

def get_ordered_content(csv_file_path):
    """Hàm lấy dữ liệu từ file CSV theo thứ tự"""
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader if row]  # Lấy cột đầu tiên của từng dòng

def write_to_csv(file_path, data, mode='a'):
    """Hàm ghi dữ liệu vào file CSV"""
    with open(file_path, mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if isinstance(data, list):
            writer.writerow(data)
        else:
            writer.writerow([data])

def update_csv_files(current_link, linknew_path, linkold_path):
    """Hàm cập nhật file CSV: xóa link hiện tại khỏi linknew.csv và thêm vào linkold.csv"""
    # Đọc nội dung từ linknew.csv
    with open(linknew_path, mode='r', encoding='utf-8') as file:
        rows = list(csv.reader(file))

    # Lọc bỏ link hiện tại
    updated_rows = [row for row in rows if row and row[0] != current_link]

    # Ghi lại nội dung mới vào linknew.csv
    with open(linknew_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    # Thêm link hiện tại vào linkold.csv
    write_to_csv(linkold_path, current_link)

def is_duplicate(link, linkold_path):
    """Hàm kiểm tra xem link có tồn tại trong linkold.csv không"""
    with open(linkold_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        old_links = [row[0] for row in reader if row]
    return link in old_links

def main_loop():
    """Vòng lặp chính của chương trình"""
    csv_file_path = make_path('csv/linknew.csv')  # Đường dẫn tới file CSV mới
    old_csv_file_path = make_path('csv/linkold.csv')  # Đường dẫn tới file CSV cũ
    contents = get_ordered_content(csv_file_path)  # Lấy toàn bộ nội dung từ file CSV
    content_index = 0  # Bắt đầu từ dòng đầu tiên

    iteration = 0
    while content_index < len(contents):
        current_content = contents[content_index]  # Lấy nội dung hiện tại

        # Kiểm tra trùng lặp
        if is_duplicate(current_content, old_csv_file_path):
            print(f"Duplicate found: {current_content}, removing from linknew.csv")
            update_csv_files(current_content, csv_file_path, old_csv_file_path)  # Xóa link trùng khỏi linknew.csv
            contents = get_ordered_content(csv_file_path)  # Cập nhật lại danh sách nội dung
            continue  # Chuyển sang link tiếp theo

        iteration += 1
        pyperclip.copy(current_content)  # Copy link vào clipboard
        print(f"[{iteration}] Copy link: {current_content}")

        # Thực hiện các hành động do bạn định nghĩa
        time.sleep(2)
        find_and_click(make_path('img/autocty/newtab.png'))
        time.sleep(2)
        # Paste nội dung
        pyautogui.hotkey('ctrl', 'v')
        print("Paste dữ liệu thành công.")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(8)
        find_and_click(make_path('img/autocty/opencrawl.png'))
        time.sleep(3)
        find_and_click(make_path('img/autocty/loadsp.png'))
        time.sleep(3)
        find_and_click(make_path('img/autocty/cate.png'))
        time.sleep(3)
        # find_and_click(make_path('img/autocty/ts1.png'))
        # time.sleep(3)
        find_and_click(make_path('img/autocty/sws1.png'))
        time.sleep(3)
        pyautogui.scroll(-1200)
        time.sleep(2)
        find_and_click(make_path('img/autocty/save.png'))
        time.sleep(6)
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
