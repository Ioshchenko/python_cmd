import argparse
from validator import validate

parser = argparse.ArgumentParser(description='Console utility for generating test data based on provided data schema')
parser.add_argument('-path_to_save_files', help='Where all files need to save')



def generate(args):
    result = validate(args)
    if result:
        print(f'Error: {result}')
    else:
        print('generate')


if __name__ == '__main__':
    args = parser.parse_args()
    generate(args)
