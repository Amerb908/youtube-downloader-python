import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    if url:
        try:
            ydl_opts = {
                'outtmpl': 'downloaded vid\\%(title)s.%(ext)s'  #choose the location you want to save your video. By default, it will save it in the current directory
            }
            #this downloads the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please enter a valid URL")

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x100")

url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download as MP4", command=download_video)
download_button.pack()

root.mainloop()

