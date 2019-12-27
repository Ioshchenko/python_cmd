import json
import random
import uuid
from pathlib import Path
from console_exception import ConsoleException
import os


def save(lines, params):
    folder = _get_path(params)
    for i in range(params.files_count):
        file_path = folder.joinpath(_get_file_name(i, params))
        with open(file_path, 'w') as file:
            json.dump(lines, file)


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
