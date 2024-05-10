# mp3-dl

Download youtube videos as .mp3 files

**Note**: requires [https://ffmpeg.org/download.html](ffmpeg) to be installed on your system.

How to use (CLI):
- Download & run `python3 mp3-dl.py`.
- set `DOWNLOAD_PATH` to the desired location where files will be downloaded to.
- If no arguments are specified, repeatedly prompts the terminal for a youtube link to download.  Press enter on a new line to stop.
- If `-f` is specified, downloads all links in `LIST_PATH`.  Put a separate link on each line in the list.

How to use (GUI):
- Download & run `python3 mp3-dl-app.py`.
- Paste links into the GUI and click download.
- Note: you can specify whether to allow popup alerts or suppress `ffmpeg` command outputs in the `mp3-dl-app.py`.  Popup alerts and command outputs are disabled by default, and files with the same name will be replaced by default.
