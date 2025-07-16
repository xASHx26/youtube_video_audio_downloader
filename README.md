Python must be installed  
# **How to Install the YouTube Downloader**

---

## 📥 Prerequisites

Before you proceed, make sure you have the following installed:

### ✅ Install Python

1. Download from: [https://www.python.org/downloads](https://www.python.org/downloads)
2. During installation, check:  
☑ Add Python to PATH

perl
Copy
Edit

### ✅ Install yt-dlp

After installing Python, open **Command Prompt** and run:


pip install yt-dlp
✅ Install ffmpeg (Recommended)
Download from: https://www.gyan.dev/ffmpeg/builds

Extract the ZIP to C:\ffmpeg

Add C:\ffmpeg\bin to your System Environment Variables > Path

Test with:

bash
Copy
Edit
ffmpeg -version
🛠️ Script Setup
Download the Scripts File

Download the provided script file for YouTube Downloader.

Do not change the file name.

Copy the File to C:\

Copy the script file and paste it into the C:\ directory.

Edit the System Environment Variables

Open Control Panel > System and Security > System > Advanced system settings.

Alternatively, search for "Edit the system environment variables" in the Windows search bar.

Press "Environment Variables"

In the System Properties window, click on Environment Variables.


Edit the System Variables

Under System variables, locate the variable Path and click Edit.

Click New to add a new path.



Add the Path to C:\scripts

Add C:\scripts as a new path entry.

Click OK to save changes.


▶️ How to Use
Run the Script Using CMD

Open Command Prompt (CMD).

Use the following command:

bash
Copy
Edit
pyd <YouTube Link>
Replace <YouTube Link> with the URL of the video or audio you want to download.

Choose the Download Type

After entering the command, the script will prompt:

less
Copy
Edit
Choose download type:
1) Video
2) Audio
Enter 1 for video or 2 for audio.

Optional Quality Selection

If the video supports 4K resolution or above, the script will ask whether you want to download 4K or 1080p.

If the highest available quality is 1080p or below, it will download automatically.
