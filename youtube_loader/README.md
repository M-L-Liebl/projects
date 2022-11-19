# Youtube loader

Small python script to download youtube videos to mp3

## Requirements

See `requirements.txt`

- Python3
- pip
- yt-dlp

## How-to

- Save videos of interest in a file, e.g. `songs` with following format line by line:
  
  `filename,URL`
  
  example:
  
  `favouriteSong1,https://www.youtube.com/watch...`
  `favouriteSong2,https://www.youtube.com/watch...`

- run main.py:

  `python main.py <path_to_songs_file> <optional: path_to_target_directory>`

  all videos will be downloaded, converted to audio-mp3 files and saved in current directory if no target_directory is specified
  
