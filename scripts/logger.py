from click import secho

class Logger(object):
    def success(self, message: str):
        self.display("[ SUCCESS ] {}".format(message), "green")

    def info(self, message: str):
        self.display("[ INFO    ] {}".format(message), "blue")

    def warn(self, message: str):
        self.display("[ WARN    ] {}".format(message), "yellow")

    def verbose(self, message: str, verbose_flag: bool):
        if verbose_flag:
            self.display("[ DEBUG   ] {}".format(message), "cyan")

    def error(self, message: str):
        self.display("[ ERROR   ] {}".format(message), "red")

    @staticmethod
    def display(formatted_message, color):
        secho(formatted_message, fg=color)