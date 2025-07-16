How to Install the YouTube Downloader
Python must be installed
1. Download the Script File
Download the provided script file for YouTube Downloader.
Do not change the file name.
2. Copy the File to C:\
Copy the script file and paste it into the C:\ directory.
☑ Ensure Python is added to the system PATH during installation.
3. Install Dependencies
Install yt-dlp: Open Command Prompt and run:
pip install yt-dlp
Install ffmpeg (Recommended):
Download from: https://www.gyan.dev/ffmpeg/builds
Extract the ZIP to: C:\ffmpeg
Add C:\ffmpeg\bin to your System Environment Variables > Path
Test installation with: ffmpeg -version
4. Edit the System Environment Variables
Open: Control Panel > System and Security > System > Advanced system settings
Or search: 'Edit the system environment variables' in the Start Menu
5. Open Environment Variables
In the System Properties window, click on Environment Variables.
Image: https://github.com/user-attachments/assets/d30a333e-1279-47c3-a85f-ce88ddf53c13
6. Edit the System Path Variable
Under System variables, find Path and click Edit.
Click New to add a new path.
Image: https://github.com/user-attachments/assets/2d3d7cf0-a57f-4e19-b1cc-b999505c7e15
7. Add the Path to C:\scripts
Add C:\scripts as a new path entry.
Click OK to save changes.
Image: https://github.com/user-attachments/assets/38dc1909-5033-46fc-ad5c-b5a86f86b06a
8. Run the Script Using CMD
Open Command Prompt (CMD)
Run the command: pyd <YouTube Link>
Replace <YouTube Link> with the actual video or playlist URL
9. Choose the Download Type
The script will prompt:
Choose download type:
1) Video
2) Audio
Enter 1 for video or 2 for audio.
10. Optional Quality Selection
If the video supports 4K, you'll be prompted to choose between 4K and 1080p.
If 1080p or lower, it will download automatically.
