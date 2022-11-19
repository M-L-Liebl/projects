import os

# save songs in this kind of format line per line: URL,SongName

def getUrls()->dict:
    songs = dict()
    with open("songs","r") as f:
        lines = [line for line in f]
    for line in lines:
        songs[line.split(",")[0]] = line.split(",")[1]
    return songs

def loadSongs()->None:
    songs = getUrls()
    for song in songs:
        os.system(f"yt-dlp -x --audio-format mp3 --audio-quality 0 -o '{songs[song].strip()}.mp3' {song.strip()}")
        
if __name__=="__main__":
    loadSongs()
