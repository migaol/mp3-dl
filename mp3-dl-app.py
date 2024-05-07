import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os

DEFAULT_PATH = os.path.expanduser("~/Downloads")

def download_audio(link: str, download_path: str):
    try:
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()
        file_path = audio.download(output_path=download_path)
        messagebox.showinfo("Download Complete", f"Downloaded: {yt.title}")
        to_mp3(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

def to_mp3(file_path: str):
    stem, ext = os.path.splitext(file_path)
    mp3_path = stem + ".mp3"
    if os.path.exists(mp3_path):
        overwrite = messagebox.askyesno("File Exists", f"The file '{mp3_path}' already exists. Do you want to overwrite it?")
        if not overwrite: return
    os.system(f'ffmpeg -i "{file_path}" "{mp3_path}"')
    os.remove(file_path)

def choose_download_directory(download_directory_label: tk.Label, download_path: str):
    download_path = filedialog.askdirectory(initialdir=download_path)
    download_directory_label.config(text=f"Download Directory: {download_path}")

def main():
    root = tk.Tk()
    root.title("YouTube Audio Downloader")

    download_path = DEFAULT_PATH

    download_directory_label = tk.Label(root, text=f"Download Directory: {download_path}")
    download_directory_label.pack()

    choose_directory_button = tk.Button(root, text="Choose Download Directory", command=lambda: choose_download_directory(download_directory_label, download_path))
    choose_directory_button.pack()

    label = tk.Label(root, text="Enter YouTube link:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    download_button = tk.Button(root, text="Download", command=lambda: download_audio(entry.get(), download_path))
    download_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()