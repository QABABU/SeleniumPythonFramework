import inspect
import logging


class ConsoleLogger:

    @staticmethod
    def get_logger(logger_name):
        # logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        console_header = logging.StreamHandler()
        console_header.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%d:%m:%Y %I:%M:%S %p')

        # add formatter to console handler
        console_header.setFormatter(formatter)

        logger.addHandler(console_header)

        return logger


