#USING pytube and moviepy
import pytube
import glob 
import os
from moviepy.editor import *


#get songs from file
filePath = open('songs.txt','r')

for link in filePath:
    try:
        print("Downloading: "+link[:-1])
        yt = pytube.YouTube(link)
        stream = yt.streams.get_audio_only()
        stream.download(output_path="downloaded_songs/")
    except:
        print("Download Failed!")
    

os.chdir("downloaded_songs/")
for file in glob.glob("*.mp4"):
    #print(file)
    try:
        video = AudioFileClip(file)
        file_mp3 = "../downloaded_songs_mp3/"+file[:-1]+"3"
        video.write_audiofile(file_mp3);
    except:
        print("mp3 conversion failed!")