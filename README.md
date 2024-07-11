# mp3-dl

Download youtube videos as .mp3 files

How to use (GUI):
- Download `mp3-dl-app` in the `dist` folder.  Then double click to run.
- Paste links into the GUI and click download.
- Alternatively, download & run `python3 mp3-dl-app.py`.

How to use (CLI):
- Download & run `python3 mp3-dl.py`.
- set `DOWNLOAD_PATH` to the desired location where files will be downloaded to.
- If no arguments are specified, repeatedly prompts the terminal for a youtube link to download.  Press enter on a new line to stop.
- If `-f` is specified, downloads all links in `LIST_PATH`.  Put a separate link on each line in the list.
