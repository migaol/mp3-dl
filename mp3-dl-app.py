import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL
import os

ALLOW_ALERTS = False # allow popup message boxes
DEFAULT_PATH = os.path.expanduser("~/Downloads")

def set_label(label: tk.Label, s: str):
    label.config(text=s)
    label.update_idletasks()

def download_audio(link: str, dl_path: str, status_label: tk.Label):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(dl_path, '%(title)s.%(ext)s')
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            set_label(status_label, "Downloading...")
            ydl.download(link)
            
            if ALLOW_ALERTS: messagebox.showinfo("Download Complete")
            set_label(status_label, "Done!")
        except Exception as e:
            if ALLOW_ALERTS: messagebox.showerror("Error", f"Download failed: {e}")
            else: set_label(status_label, f"Download failed: {e}")

def main():
    root = tk.Tk()
    root.title("YouTube Audio Downloader")

    dl_path = DEFAULT_PATH
    def choose_dir(dl_dir_label: tk.Label, dl_path: str):
        dl_path = filedialog.askdirectory(initialdir=dl_path)
        dl_dir_label.config(text=f"Download Directory: {dl_path}")

    dl_dir_label = tk.Label(root, text=f"Download Directory: {dl_path}")
    dl_dir_label.pack()

    choose_dir_btn = tk.Button(root, text="Choose Download Directory", command=lambda: choose_dir(dl_dir_label, dl_path))
    choose_dir_btn.pack()

    label = tk.Label(root, text="Enter YouTube link:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    status_label = tk.Label(root, text="")
    status_label.pack()

    dl_btn = tk.Button(root, text="Download", command=lambda: download_audio(entry.get(), dl_path, status_label))
    dl_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()