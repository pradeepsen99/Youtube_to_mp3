from logger import Logger
class Config(object):
    __slots__ = ["verbose", "logger", "yt_dl_path", "convert_path", "workers", "out_format"]

    # General configuration options
    def __init__(self, verbose: bool, yt_dl_path: str, convert_path: str, workers: int, out_format: str):
        self.verbose = verbose
        self.logger = Logger()
        self.yt_dl_path = yt_dl_path
        self.convert_path = convert_path
        self.workers = workers
        self.out_format = out_format