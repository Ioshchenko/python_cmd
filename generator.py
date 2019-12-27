import argparse
import json
import sys
import uuid

import shema
import utils
import random
from console_exception import ConsoleException

parser = argparse.ArgumentParser(description='Console utility for generating test data based on provided data schema')
parser.add_argument('-path_to_save_files', help='Where all files need to save.')
parser.add_argument('-data_schema', help='Json schema.')
parser.add_argument('-data_lines', help='Count of lines for each file.', nargs='?', const=1, type=int, default=3)
parser.add_argument('-files_count', help='Json file count. If files_count = 0 print all output to console.', type=int,
                    default=1)
parser.add_argument('-file_name', help='Base file_name.', default='data')
parser.add_argument('-file_prefix', help='Prefix for file name to use if it more that 1 file.', default='count1')


def generate(params):
    lines = shema.generate(params.data_schema, params.data_lines)
    files_count = utils.get_file_count(params.files_count)
    if files_count == 0:
        print(json.dumps(lines, indent=2))
    else:
        folder = utils.get_path(params)
        for i in range(files_count):
            file_path = folder.joinpath(get_file_name(i, params))
            with open(file_path, 'w') as file:
                json.dump(lines, file)


def get_file_name(i, params):
    return '{}_{}.json'.format(params.file_name, get_prefix(params.file_prefix, i))


def get_prefix(file_prefix, index):
    switcher = {
        "count": lambda: index,
        "random": lambda: random.randint(1, 9999),
        "uuid": lambda: str(uuid.uuid4())
    }
    func = switcher.get(file_prefix)
    if not func:
        raise ConsoleException('Wrong prefix type: {}'.format(file_prefix))
    return func()


if __name__ == '__main__':
    try:
        print("Start")
        generate(parser.parse_args())
        print("Finish")
    except ConsoleException as e:
        print('Error: {}'.format(e.message))
        sys.exit(1)
