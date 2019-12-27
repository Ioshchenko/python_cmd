from os import path


def validate(args):
    dir_path = args.path_to_save_files
    if path.isabs(dir_path):
        dir_path = path.join(path.dirname(__file__), dir_path)
    if not path.exists(dir_path):
        return 'Path {} is not exist.'.format(dir_path)
    if not path.isdir(dir_path):
        return 'Path {} is not a directory.'.format(dir_path)
