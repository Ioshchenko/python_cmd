import argparse
import json
import shema
from validator import validate

parser = argparse.ArgumentParser(description='Console utility for generating test data based on provided data schema')
parser.add_argument('-path_to_save_files', help='Where all files need to save.')
parser.add_argument('-data_schema', help='Json schema.')
parser.add_argument('-data_lines', help='Count of lines for each file.', nargs='?', const=1, type=int, default=3)
args = parser.parse_args()


def generate(params):
    res = validate(params)
    lines = shema.generate(params.data_schema, params.data_lines)
    with open('data.json', 'w') as file:
        json.dump(lines, file)


if __name__ == '__main__':
    print("Start")
    generate(args)
