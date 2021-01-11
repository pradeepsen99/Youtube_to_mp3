#USING pytube and moviepy
import pytube
import converter

from config import Config
from pathlib import Path
from multiprocessing import Pool

# Temporary class to enable multiprocessing down below
class DLConfig:
    __slots__ = ["link", "config"]

    def __init__(self, link: str, config: Config):
        self.link = link
        self.config = config

# Download from a specific file containing the list of links
def download_from_file(file_path: str, config: Config):
    logger = config.logger
    with open(file_path) as file:
        song_list = [i.strip() for i in file]
        song_list = [ 
            DLConfig(
                link=link,
                config=config
            ) for link in song_list
        ]
        logger.verbose("Starting download worker processes...", config.verbose)
        with Pool(processes=config.workers) as worker:
            worker.map(download, song_list)
    logger.verbose("Exiting download process.", config.verbose)


# Just a dumb wrapper around the download function
def download_from_link(link: str, config: Config):
    dlconfig = DLConfig(link, config)
    download(dlconfig)

# Download a video file from a single link
def download(dlconfig: DLConfig):
    try:
        logger = dlconfig.config.logger
        yt = pytube.YouTube(dlconfig.link)
        logger.info("Downloading <= '{}'".format(yt.title))
        if not Path(dlconfig.config.yt_dl_path).exists():
            Path(dlconfig.config.yt_dl_path).mkdir(exist_ok=True)
        yt.streams.first().download(output_path=dlconfig.config.yt_dl_path)
        logger.success("Downloaded : '{}'".format(yt.title))
    except Exception as e:
        logger.error("Download Failed:\n{}".format(e))