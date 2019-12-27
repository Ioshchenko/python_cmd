from pathlib import Path
from console_exception import ConsoleException
import os


def get_path(args):
    dir_path = args.path_to_save_files
    path = Path(dir_path)
    if not path.is_absolute():
        path = Path(os.getcwd()).joinpath(dir_path)
    if not path.exists():
        raise ConsoleException('Path {} is not exist.'.format(dir_path))
    if not path.is_dir():
        raise ConsoleException('Path {} is not a directory.'.format(dir_path))
    return path


def get_file_count(value):
    if value < 0:
        raise ConsoleException('File count cannot be less than 0')
    return value
