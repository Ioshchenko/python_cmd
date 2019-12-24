import argparse
from validator import validate

parser = argparse.ArgumentParser(description='Console utility for generating test data based on provided data schema')
parser.add_argument('path_to_save_files', help='Where all files need to save')
args = parser.parse_args()


def generate(args):
    res = validate(args)
    if res:
        print(res)
    else:
        print('generate')


if __name__ == '__main__':
    generate(args)
