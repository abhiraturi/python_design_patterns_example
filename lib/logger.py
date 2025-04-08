import os 
import coloredlogs
import sys

import logging
from colorlog import ColoredFormatter
import json_log_formatter


class Logger:
    _instances = {}

    def __new__(cls,logger_name: str):
        if logger_name not in cls._instances:
            instance = super(Logger, cls).__new__(cls)
            instance._initialize_logger(logger_name)
            cls._instances[logger_name] = instance
        return cls._instances[logger_name]
    
    def _initialize_logger(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)
        env = os.environ.get("ENV", "development")
        log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

        if not self.logger.hasHandlers():
            if env == "development":
                self._install_colored_logs(log_level)
            else:
                self._add_json_formatter(log_level)

    def _install_colored_logs(self, log_level):
        coloredlogs.install(
            logger=self.logger,
            fmt="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d - %(funcName)s()] %(message)s",
            level=log_level,
        )

    def _add_json_formatter(self, log_level):
        formatter = json_log_formatter.VerboseJSONFormatter()
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        self.logger.setLevel(log_level)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger