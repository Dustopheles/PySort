"""Config module."""

import os
from configparser import ConfigParser

class Config():
    """Config base class."""
    path = 'config.ini'
    config = ConfigParser()

    @staticmethod
    def read_config() -> None:
        """Read config file if exists."""
        if not os.path.exists(Config.path):
            print(f"[ERR] {Config.path} not found!")
            return
        Config.config.read(Config.path)

    @staticmethod
    def write_config() -> None:
        """Write config to file if exists."""
        if not os.path.exists(Config.path):
            print(f"[ERR] {Config.path} not found!")
            return
        with open(Config.path, 'w+', encoding='utf8') as file:
            Config.config.write(file)
