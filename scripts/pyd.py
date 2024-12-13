import yt_dlp
import os
import sys

def get_unique_filename(download_path, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    unique_filename = filename
    while os.path.exists(os.path.join(download_path, unique_filename)):
        unique_filename = f"{base} ({counter}){ext}"
        counter += 1
    return unique_filename

def download(link, download_type):
    download_path = r"D:\Downlowd\youtube downlowd"
    if not os.path.exists("D:"):
        download_path = os.path.join(os.path.expanduser("~"), "Downloads", "youtube_downloading")

    os.makedirs(download_path, exist_ok=True)

    if download_type == "video":
        filename_template = '%(title)s.%(ext)s'
    elif download_type == "audio":
        filename_template = '%(title)s.%(ext)s'
    else:
        print("Invalid download type. Please choose 'video' or 'audio'.")
        sys.exit(1)

    options = {'outtmpl': os.path.join(download_path, filename_template)}
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(link, download=False)
        title = info.get('title', 'video')
        ext = info.get('ext', 'mp4' if download_type == "video" else 'm4a')

    unique_filename = get_unique_filename(download_path, f"{title}.{ext}")

    options = {
        'format': 'bestaudio+bestvideo' if download_type == "video" else 'bestaudio',
        'outtmpl': os.path.join(download_path, unique_filename),
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pyd <video_link>")
        sys.exit(1)

    video_link = sys.argv[1]

    print("Choose download type:")
    print("1) Video")
    print("2) Audio")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        download_type = "video"
    elif choice == "2":
        download_type = "audio"
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit(1)

    download(video_link, download_type)
