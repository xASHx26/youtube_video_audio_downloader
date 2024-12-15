
# **How to Install the YouTube Downloader**

1. **Download the Scripts File**  
   - Download the provided script file for YouTube Downloader.  
   - **Do not change the file name**.

2. **Copy the File to `C:\`**  
   - Copy the script file and paste it into the `C:\` directory.

3. **Edit the System Environment Variables**  
   - Open **Control Panel** > **System and Security** > **System** > **Advanced system settings**.  
   - Alternatively, search for **"Edit the system environment variables"** in the Windows search bar.

4. **Press "Environment Variables"**  
   - In the **System Properties** window, click on **Environment Variables**.  
   ![image](https://github.com/user-attachments/assets/d30a333e-1279-47c3-a85f-ce88ddf53c13)

5. **Edit the System Variables**  
   - Under **System variables**, locate the variable **Path** and click **Edit**.  
   - Click **New** to add a new path.

   ![image](https://github.com/user-attachments/assets/2d3d7cf0-a57f-4e19-b1cc-b999505c7e15)

6. **Add the Path to `C:\scripts`**  
   - Add `C:\scripts` as a new path entry.  
   - Click **OK** to save changes.  
   ![image](https://github.com/user-attachments/assets/38dc1909-5033-46fc-ad5c-b5a86f86b06a)

7. **Run the Script Using CMD**  
   - Open **Command Prompt** (CMD).  
   - Use the following command:  
     ```bash
     pyd <YouTube Link>
     ```
   - Replace `<YouTube Link>` with the URL of the video or audio you want to download.

8. **Choose the Download Type**  
   - After entering the command, the script will prompt:  
     ```
     Choose download type:
     1) Video
     2) Audio
     ```  
   - Enter `1` for video or `2` for audio.  

9. **Optional Quality Selection**  
   - If the video supports **4K resolution** or above, the script will ask whether you want to download **4K** or **1080p**.  
   - If the highest available quality is 1080p or below, it will download automatically.

