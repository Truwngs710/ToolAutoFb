import os

# Thư mục Downloads
downloads_folder = os.path.expanduser('~/Downloads')

# Lấy tất cả thư mục con (không cần điều kiện tên bắt đầu bằng 'cn')
subfolders = [f.path for f in os.scandir(downloads_folder) if f.is_dir()]

# Các đuôi file cần đổi
file_extensions = ['.mp4']

for folder in subfolders:
    # Lấy danh sách file mp4 trong từng thư mục con
    files = [f for f in os.listdir(folder) if any(f.lower().endswith(ext) for ext in file_extensions)]
    files.sort()

    # Bước 1: Đổi tên tạm để tránh trùng
    temp_files = []
    for idx, filename in enumerate(files, start=1):
        old_path = os.path.join(folder, filename)
        temp_filename = f"temp_{idx}{os.path.splitext(filename)[1]}"
        temp_path = os.path.join(folder, temp_filename)
        os.rename(old_path, temp_path)
        temp_files.append(temp_filename)

    # Bước 2: Đổi thành số 1, 2, 3...
    for idx, temp_filename in enumerate(temp_files, start=1):
        temp_path = os.path.join(folder, temp_filename)
        final_filename = f"{idx}{os.path.splitext(temp_filename)[1]}"
        final_path = os.path.join(folder, final_filename)
        os.rename(temp_path, final_path)
        print(f"Renamed in {folder}: {temp_filename} -> {final_filename}")

print("✅ Hoàn tất đổi tên file mp4 trong tất cả thư mục con!")
