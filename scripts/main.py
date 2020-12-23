import os
import sys
import argparse
sys.path.append(os.path.dirname(__file__)) # Temporary fix for the ModuleNotFoundError for custom modules

import click
from converter import convert as conv
from pathlib import Path
from config import Config
from conversionjob import ConversionJob
from song_downloader import download_from_link, download_from_file
from logger import Logger

def setupParser():
    parser = argparse.ArgumentParser(description="Download and convert YouTube video content to specified audio formats")
    parser.add_argument('songs_file', metavar='songs_file', type=str, help='Path to the file containing all of the YouTube links')
    parser.add_argument('export_path', metavar='export_path', type=str, help='Path where to convert the downloaded audio')
    parser.add_argument('-w', '--workers', default=5, type=int, help='Amount of processes to create for audio conversion (default: 5)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose for debugging purposes.')

    return parser.parse_args()

# Paste the link
def convert():

    args = setupParser()

    c = Config(
        verbose=args.verbose,
        # yt_dl_path=Path.home().as_posix() + "/Downloads/Downloaded_Videos",
        yt_dl_path=args.export_path,
        # convert_path=Path.home().as_posix() + "/Downloads/Converted_Videos",
        convert_path=args.export_path,
        workers=args.workers,
        out_format=".mp3"
    )
    #link_file = Path.home().as_posix() + "/Downloads/links.txt"
    link_file = args.songs_file

    logger = c.logger
    logger.verbose("Input : {}".format(link_file), c.verbose)
    logger.verbose("Output : {}".format(c.convert_path), c.verbose)
    logger.verbose("Workers : {}".format(c.workers), c.verbose)

    # download_from_link("testlink", c)
    download_from_file(file_path=link_file, config=c)
    conv(config=c, input_directory=c.yt_dl_path, output_directory=c.convert_path, output_format=c.out_format, workers=c.workers)
