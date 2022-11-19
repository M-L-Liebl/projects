import os
from threading import Thread
from pathlib import Path
from sys import argv
import time

# save URLS and desired file names in e.g. file "songs"
# format: URL,filename
# e.g:
# https://www.youtube.com/watch...,favouriteSong1
# https://www.youtube.com/watch...,favouriteSong2
# ...
#
# run script with: python main.py <path_to_songs_file>


def getUrls(urls_file:str)->dict:
    """
    Gets the URLS and filenames from urls_file in sys.argv[1]
    Returns:
        dict<filename:str><URL:str> 
    """
    songs = dict()
    with open(urls_file,"r") as f:
        lines = [line for line in f]
    for line in lines:
        songs[line.split(",")[0]] = line.split(",")[1]
    return songs

def loadSongs(urls_file:str, dest_directory:str="")->None:
    # check if urls_file and dest_directory exists
    my_file = Path(urls_file)
    my_file.is_file()
    if not Path(urls_file).is_file():
        print(f"urls_file {urls_file} does not exist")
        return
    if not Path(dest_directory).is_dir():
        print(f"destination directory {dest_directory} does not exist")
        return
    songs = getUrls(urls_file)
    threads = []
    for song in songs:
        load = lambda : os.system(f"yt-dlp -x --audio-format mp3 --audio-quality 0 -o '{dest_directory + songs[song].strip()}.mp3' {song.strip()}")
        thread = Thread(target = load)
        threads.append(thread)
        print(f"load {songs[song]} - {song}")
        thread.start()
    for thread in threads:
        thread.join()
        
        
        
if __name__=="__main__":
    if len(argv) == 2:
        loadSongs(argv[1])
    elif len(argv) == 3:
        loadSongs(argv[1], argv[2])
    else:
        print("You have to specify path to url_file, e.g.: python main.py song_urls")
        