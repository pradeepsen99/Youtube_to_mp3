import os
import sys
sys.path.append(os.path.dirname(__file__))

import click
import converter
from pathlib import Path
from config import Config
from conversionjob import ConversionJob
from song_downloader import download_from_link


def convert():
    c = Config(verbose=True)
    download_from_link("https://www.youtube.com/watch?v=ZLKZKmdZEjM&ab_channel=Gorillaz", c.logger)
    converter.convert(c, Path.home().as_posix() + "/Downloads/Downloaded_Songs", Path.home().as_posix() + "/Downloads", ".mp3", 5)