import argparse
import configparser
import json
import sys

import shema
import file_utils
from console_exception import ConsoleException

config = configparser.ConfigParser()
config.read('default.ini')

parser = argparse.ArgumentParser(description='Console utility for generating test data based on provided data schema',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--path_to_save_files', help='Where all files need to save.',
                    default=config['args']['path_to_save_files'])
parser.add_argument('--data_schema', help='Json schema.')
parser.add_argument('--data_lines', help='Count of lines for each file.',
                    type=int,
                    default=config['args']['data_lines'])
parser.add_argument('--files_count', help='Json file count. If files_count = 0 print all output to console.',
                    type=int,
                    default=config['args']['files_count'])
parser.add_argument('--file_name', help='Base file_name.',
                    default=config['args']['file_name'])
parser.add_argument('--file_prefix', help='Prefix for file name to use if it more that 1 file.',
                    default=config['args']['file_prefix'])
parser.add_argument('--clear_path', help='If this flag is on, before the script starts creating new data files, '
                                         'all files in path_to_save_files that match file_name will be deleted.',
                    default=config['args']['clear_path'])


def generate(params):
    lines = shema.generate(params.data_schema, params.data_lines)
    files_count = _get_file_count(params.files_count)
    if files_count == 0:
        print(json.dumps(lines, indent=2))
    else:
        file_utils.save(lines, params)


def _get_file_count(value):
    if value < 0:
        raise ConsoleException('File count cannot be less than 0')
    return value


if __name__ == '__main__':
    try:
        print("Start")
        generate(parser.parse_args())
        print("Finish")
    except ConsoleException as e:
        print('Error: {}'.format(e.message))
        sys.exit(1)
