# Short Python script to download YouTube audio

from typing import List
from yt_dlp import YoutubeDL
import os, argparse

DOWNLOAD_PATH = "/Users/michael/Downloads" # replace with the desired download directory
LIST_PATH = "/Users/michael/Desktop/m/ytmp3.txt" # directory of a file with links to dowload, one per line

def download(links: List[str], suppress: bool = True) -> None:
    def progress_hook(dl):
        if dl['status'] == 'finished': print(f" Downloaded: {dl['filename']}")

    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s')
    }
    if suppress:
        ydl_opts['quiet'] = True
        ydl_opts['progress_hooks'] = [progress_hook]

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
def main(args: argparse.Namespace) -> None:
    links = []
    if args.file:
        with open(LIST_PATH, 'r') as f:
            links = [line.strip() for line in f.readlines()]
    else:
        while (link := input("$ ")):
            links.append(link)
    
    download(links, suppress=args.no_output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download YouTube audio")
    parser.add_argument('-f', '--file', action='store_true', help='Path to a text file containing YouTube links')
    parser.add_argument('-s', '--no-output', action='store_true', help='Suppress ffmpeg output', default=True)
    args = parser.parse_args()
    main(args)
    print("Done")
