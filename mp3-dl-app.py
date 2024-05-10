import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os

SUPPRESS_OUTPUT = False # suppress ffmpeg command outputs
ALLOW_ALERTS = False # allow popup message boxes
DEFAULT_PATH = os.path.expanduser("~/Downloads")

def set_label(label: tk.Label, s: str):
    label.config(text=s)
    label.update_idletasks()

def download_audio(link: str, dl_path: str, status_label: tk.Label):
    try:
        set_label(status_label, "Finding Video...")
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()

        set_label(status_label, "Downloading...")
        file_path = audio.download(output_path=dl_path)

        set_label(status_label, "Converting...")
        to_mp3(file_path)
        
        if ALLOW_ALERTS: messagebox.showinfo("Download Complete", f"Downloaded: {yt.title}")
        set_label(status_label, "Done!")
    except Exception as e:
        if ALLOW_ALERTS: messagebox.showerror("Error", f"Download failed: {e}")
        else: set_label(status_label, f"Download failed: {e}")

def to_mp3(file_path: str):
    stem, ext = os.path.splitext(file_path)
    mp3_path = stem + ".mp3"
    if os.path.exists(mp3_path):
        if ALLOW_ALERTS:
            overwrite = messagebox.askyesno("File Exists", f"The file '{mp3_path}' already exists. Do you want to overwrite it?")
            if not overwrite: return
        os.remove(mp3_path) # remove by default
    convert_cmd = f'ffmpeg -i "{file_path}" "{stem}.mp3"'
    if SUPPRESS_OUTPUT: convert_cmd += ' > /dev/null 2>&1'

    os.system(convert_cmd)
    os.remove(file_path)

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