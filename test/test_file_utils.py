import os
import unittest
from pathlib import Path
import argparse

import file_utils
from console_exception import ConsoleException


class FileUtilsTestCase(unittest.TestCase):
    def test_should_clean_dir(self):
        path = Path(os.getcwd()).joinpath('test.dat')
        with open(path, 'w+') as f:
            f.write("data")
        file_utils.clean_dir([path])
        self.assertFalse(path.exists())

    def test_should_throw_exception(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--path_to_save_files')
        args = parser.parse_args(['--path_to_save_files', 'BAR'])
        self.assertRaises(ConsoleException, file_utils.generate_file_name, args)


if __name__ == '__main__':
    unittest.main()
