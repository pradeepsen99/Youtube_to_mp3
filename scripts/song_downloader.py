#USING pytube and moviepy
import pytube
import converter

from logger import Logger
from pathlib import Path

# Download from a specific file containing the list of links
def download_from_file(file_path: str, logger: Logger):
    songs = open(file_path)
    for link in songs:
        download(link, logger)

# Just a dumb wrapper around the download function
def download_from_link(link: str, logger: Logger):
    download(link, logger)

# Download a video file from a single link
def download(link: str, logger: Logger):
    try:
        logger.verbose("Downloading " + link[:-1], True)
        yt = pytube.YouTube(link)
        audio_stream = yt.streams.get_audio_only()
        download_path = Path.home().as_posix() + "/Downloads/Downloaded_Songs"
        if not Path(download_path).exists():
            Path(download_path).mkdir(exist_ok=True)
        audio_stream.download(output_path=download_path)
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