import os
import random
import subprocess
from pathlib import Path

# Đường dẫn thư mục
input_dir = r"C:\Users\PC\Downloads\shit"
output_dir = r"C:\Users\PC\Downloads\shitEdited"
icon_dir = r"C:\Users\PC\Desktop\code\ToolAutoFb\img\icon"

# Tạo thư mục output nếu chưa tồn tại
os.makedirs(output_dir, exist_ok=True)

# Kiểm tra quyền ghi cho thư mục output
if not os.access(output_dir, os.W_OK):
    print(f"Không có quyền ghi vào thư mục {output_dir}")
    exit()

# Lấy danh sách file video
video_extensions = (".mp4", ".mov", ".avi", ".mkv")
video_files = [f for f in os.listdir(input_dir) if f.lower().endswith(video_extensions)]

# Lấy danh sách file icon
icon_extensions = (".png", ".jpg", ".jpeg")
icon_files = [f for f in os.listdir(icon_dir) if f.lower().endswith(icon_extensions)]

# Kiểm tra xem có icon nào không
if not icon_files:
    print("Không tìm thấy file icon trong thư mục C:\\Users\\PC\\Downloads\\icon")
    exit()

for video in video_files:
    input_path = os.path.join(input_dir, video)
    output_path = os.path.join(output_dir, f"{video}")
    
    # Kiểm tra file video có tồn tại và đọc được không
    if not os.path.exists(input_path):
        print(f"File video không tồn tại: {input_path}")
        continue
    
    # Chọn icon ngẫu nhiên
    random_icon = random.choice(icon_files)
    icon_path = os.path.join(icon_dir, random_icon)
    
    # Kiểm tra file icon có tồn tại và đọc được không
    if not os.path.exists(icon_path):
        print(f"File icon không tồn tại: {icon_path}")
        continue
    
    # Lệnh FFmpeg:
    # - Xoay video 5 độ
    # - Thêm icon ở góc trên trái
    # - Mute audio 0.5s đầu tiên
    ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_path,  # Input video
    "-i", icon_path,  # Input icon ngẫu nhiên
    "-filter_complex", "[0:v]rotate=2*PI/180[v];[v]drawbox=x=0:y=550:w=iw:h=1:color=white:t=fill[v1];[1:v]scale=iw/6:ih/6[icon];[v1][icon]overlay=W-w-10:(H-h)/2[vout]",
    "-map", "[vout]",  # Map video output
    "-map", "0:a?",  # Map audio (nếu có)
    "-af", "volume=0:enable='lte(t,0.1)+gte(mod(t,8),0)*lte(mod(t,8),0.1)'",
    "-c:v", "libx264",
    "-preset", "fast",
    "-c:a", "aac",
    "-y",
    output_path
]
    
    try:
        # Chạy lệnh FFmpeg
        subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
        print(f"Đã xử lý: {video} -> {output_path} (Icon: {random_icon})")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi xử lý {video}: {e}")
        print(f"FFmpeg output: {e.stderr}")
    except FileNotFoundError:
        print("Lỗi: FFmpeg không được cài đặt hoặc không tìm thấy trong PATH")
        break

print("Hoàn tất chỉnh sửa hàng loạt video!")