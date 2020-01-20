import json
import random
import uuid
from pathlib import Path
from console_exception import ConsoleException
import os
import logging


def save(lines, file_path):
    """
    Saved json objects to the file.
    :param lines: json objects
    :param file_path: file path
    """
    logging.info('Save data to the file:{}'.format(file_path))
    with open(file_path, 'w') as file:
        json.dump(lines, file)


def clean_dir(files):
    """
    Deleted files.
    :param files: list of files
    """
    for file in files:
        if os.path.exists(file):
            os.remove(file)
    logging.info('Clean up folder')


def generate_file_name(params):
    """
    Generated file names based on parameters
    :param params: params from command line
    :return: list of file names
    """
    folder = _get_path(params)
    return [folder.joinpath(_get_file_name(i, params)) for i in range(params.files_count)]


def _get_path(args):
    dir_path = args.path_to_save_files
    path = Path(dir_path)
    if not path.is_absolute():
        path = Path(os.getcwd()).joinpath(dir_path)
    if not path.exists():
        raise ConsoleException('Path {} is not exist.'.format(dir_path))
    if not path.is_dir():
        raise ConsoleException('Path {} is not a directory.'.format(dir_path))
    return path


def _get_file_name(i, params):
    return '{}_{}.json'.format(params.file_name, _get_prefix(params.file_prefix, i))


def _get_prefix(file_prefix, index):
    switcher = {
        "count": lambda: index,
        "random": lambda: random.randint(1, 9999),
        "uuid": lambda: str(uuid.uuid4())
    }
    func = switcher.get(file_prefix)
    if not func:
        raise ConsoleException('Wrong prefix type: {}'.format(file_prefix))
    return func()
