# Short Python script to download YouTube audio

from pytube import YouTube
from typing import List
import argparse

DOWNLOAD_PATH = "/Users/michael/Downloads" # replace with the desired download directory
LIST_PATH = "/Users/michael/Desktop/m/ytmp3.txt" # directory of a file with links to dowload, one per line

def download(links: List[str]) -> None:
    for url in links:
        try:
            print(f"Downloading: ", end="")
            yt = YouTube(url)
            print(f"{yt.title[:30]}... ", end="")
            audio = yt.streams.filter(only_audio=True).first()
            
            output_file = f"{yt.title}.mp3"
            audio.download(output_path=DOWNLOAD_PATH, filename=output_file)
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
    
    download(links)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download YouTube audio")
    parser.add_argument('-f', '--file', action='store_true', help='Path to a text file containing YouTube links')
    args = parser.parse_args()
    main(args)
    print("Done")