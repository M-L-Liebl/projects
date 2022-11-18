import os
import logging

# save songs in this kind of format line per line: URL,SongName

def getUrls()->dict:
    songs = dict()
    with open("songs.txt","r") as f:
        lines = [line for line in f]
    for line in lines:
        songs[line.split(",")[0]] = line.split(",")[1]
    return songs

def loadSongs()->None:
    logging.info("get URLS...")
    songs = getUrls()
    logging.info("got URLS")
    for song in songs:
        logging.info("load song")
        os.system(f"yt-dlp -x --audio-format mp3 --audio-quality 0 -o '{songs[song].strip()}.mp3' {song.strip()}")
        logging.info("------------------song loaded-------------------")
        
        
if __name__=="__main__":
    logging.info("started")
    loadSongs()
    logging.info("finished")
    