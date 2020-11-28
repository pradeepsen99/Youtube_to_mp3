from pathlib import Path
from typing import Optional
from logger import Logger
class ConversionJob(object):
    __slots__ = ["output_format", "verbose", "output_path", "file_path", "logger"]

    def __init__(
        self,
        output_format: str,
        verbose: bool,
        output_path: Path,
        file_path: Path,
        logger: Optional[Logger] = None
    ):
        self.output_format = output_format
        self.verbose = verbose
        self.output_path = output_path
        self.file_path = file_path
        self.logger = logger if logger is not None else Logger()