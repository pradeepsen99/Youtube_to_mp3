#USING pytube and moviepy
import pytube
import converter

from config import Config
from pathlib import Path

# Download from a specific file containing the list of links
def download_from_file(file_path: str, config: Config):
    songs = open(file_path)
    for link in songs:
        download(link, config)
    songs.close()

# Just a dumb wrapper around the download function
def download_from_link(link: str, config: Config):
    download(link, config)

# Download a video file from a single link
def download(link: str, config: Config):
    try:
        logger = config.logger
        logger.verbose("Downloading " + link[:-1], True)
        yt = pytube.YouTube(link)
        audio_stream = yt.streams.get_audio_only()
        if not Path(config.yt_dl_path).exists():
            Path(config.yt_dl_path).mkdir(exist_ok=True)
        audio_stream.download(output_path=config.yt_dl_path)
        logger.success("Downloaded " + link[:-1])
    except Exception as e:
        logger.error("Download Failed:\n{}".format(e))


# os.chdir("downloaded_songs/")

'''
for file in glob.glob("*.mp4"):
    #print(file)
    try:
        video = AudioFileClip(file)
        file_mp3 = "../downloaded_songs_mp3/"+file[:-1]+"3"
        video.write_audiofile(file_mp3);
    except:
        print("mp3 conversion failed!")
'''