import logging
import pathlib

LOG_FILE = pathlib.Path("ログファイル.log")
LOG_FORMAT = "(%(levelname)s) [%(asctime)s] %(message)s"

formatter = logging.Formatter(LOG_FORMAT)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler, file_handler],
    datefmt="%Y/%m/%d %H:%M:%S",
)
