from logger import Logger
from pydub import AudioSegment
from multiprocessing import Pool
from typing import Sequence
from config import Config
from pathlib import Path
from conversionjob import ConversionJob
from os import remove as remove_file

AUDIO_EXTENSIONS = [
    ".aiff",
    ".flac",
    ".m4a",
    #".mp3", temporary fix to avoid the pre-existing .mp3 file conversion to .mp3 format.
    ".mp4",
    ".wav",
]

AUDIO_EXTENSIONS_SET = set(AUDIO_EXTENSIONS)

# Convert the files in the input_directory and place them in the output_directory
def convert(config: Config, input_directory: str, output_directory: str, output_format: str, workers: int):
    logger = config.logger
    logger.info("Starting conversion of {}.".format(input_directory))

    input_path = Path(input_directory)
    output_path = Path(output_directory)

    if not output_path.exists():
        logger.verbose(
            "Creating output directory {}".format(output_path.as_posix()),
            config.verbose
        )
        output_path.mkdir(exist_ok=True)
    
    audio_files = get_audio_files(input_path)
    audio_files = [
        ConversionJob(
            output_format = output_format,
            verbose = config.verbose,
            output_path = output_path,
            file_path = file_path,
            logger = logger
        ) for file_path in audio_files
    ]
    logger.verbose("Starting the conversion worker processes...", config.verbose)
    with Pool(processes=workers) as worker:
        worker.map(converter, audio_files)

    logger.success("See {} for converted audio.".format(output_path.as_posix()))

# Recursively search for files in the given input_path
# TODO Make sure that already converted files would not be converted again.
def get_audio_files(input_path: Path) -> Sequence[Path]:
    audio_files = []
    for input_file in input_path.iterdir():
        if input_file.is_file() and input_file.suffix.lower() in AUDIO_EXTENSIONS_SET:
            audio_files.append(input_file)
        elif input_file.is_dir() and not input_file.is_symlink():
            audio_files.extend(get_audio_files(input_file))
    return audio_files

def converter(conversion_job: ConversionJob):
    logger = conversion_job.logger

    # Conversion specific data
    output_format = conversion_job.output_format[1:]
    output_path = conversion_job.output_path
    # verbose_flag = conversion_job.verbose

    # File specific data
    audio_file = conversion_job.file_path
    audio_name = audio_file.name[: audio_file.name.rfind(".")]
    converted_name = "{}.{}".format(audio_name, output_format)

    logger.info(
        "Converting '{}' => '{}'...".format(audio_name, output_format)
    )

    audio = AudioSegment.from_file(audio_file.as_posix(), audio_file.suffix[1:])
    output_name = output_path.joinpath(converted_name)
    audio.export(output_name.as_posix(), format=output_format, bitrate="192k",)

    logger.warn("'{}' converted! Removing video file...".format(audio_name))

    try:
        remove_file(audio_file)
        logger.success("'{}' removed".format(audio_file))
    except:
        logger.error("Could not remove '{}'".format(audio_file))
