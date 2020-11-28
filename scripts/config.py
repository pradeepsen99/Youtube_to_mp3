from logger import Logger
class Config(object):
    __slots__ = ["verbose", "logger"]

    def __init__(self, verbose: bool):
        self.verbose = verbose
        self.logger = Logger()