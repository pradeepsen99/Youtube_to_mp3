import os
import sys
sys.path.append(os.path.dirname(__file__)) # Temporary fix for the ModuleNotFoundError for custom modules

import click
from converter import convert as conv
from pathlib import Path
from config import Config
from conversionjob import ConversionJob
from song_downloader import download_from_link, download_from_file

# Paste the link
def convert():
    c = Config(
        verbose=True,
        yt_dl_path=Path.home().as_posix() + "/Downloads/Downloaded_Videos",
        convert_path=Path.home().as_posix() + "/Downloads/Converted_Videos",
        workers=5,
        out_format=".mp3"
    )

    # download_from_link("testlink", c)
    download_from_file(file_path=Path.home().as_posix() + "/Downloads/songs.txt", config=c)
    conv(config=c, input_directory=c.yt_dl_path, output_directory=c.convert_path, output_format=c.out_format, workers=c.workers)