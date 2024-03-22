# Short Python script to download YouTube audio
# Note: if the script appears to freeze and ffmpeg output is suppressed,
#       it may be that ffmpeg is waiting for input on whether to replace a file
#       so just press enter and the script should continue

from pytube import YouTube
from typing import List
import os, argparse

DOWNLOAD_PATH = "/Users/michael/Downloads" # replace with the desired download directory
LIST_PATH = "/Users/michael/Desktop/m/ytmp3.txt" # directory of a file with links to dowload, one per line

def download(links: List[str], suppress: bool = True) -> None:
    for url in links:
        try:
            print(f"Downloading: ", end="")
            yt = YouTube(url)
            print(f"{yt.title}", end="")
            
            audio = yt.streams.get_audio_only()

            audio.download(output_path=DOWNLOAD_PATH)
            file_path = os.path.join(DOWNLOAD_PATH, audio.default_filename)

            stem, ext = os.path.splitext(file_path)
            convert_cmd = f'ffmpeg -i "{file_path}" "{stem}.mp3"'
            if suppress: convert_cmd += ' > /dev/null 2>&1'

            os.system(convert_cmd)
            os.remove(file_path)
            
            print(f"Finished")
        except Exception as e:
            print(f"Error {e}\nDownload failed: {yt.title}")
    
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
