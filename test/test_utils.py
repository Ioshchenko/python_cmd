import os
import unittest
from pathlib import Path

import file_utils
from console_exception import ConsoleException


class UtilTestCase(unittest.TestCase):
    def test_should_clean_dir(self):
        path = Path(os.getcwd()).joinpath('test.dat')
        with open(path, 'w+') as f:
            f.write("data")
         file_utils.clean_dir([path])
        # self.assertFalse(path.exists())



#def test_should_throw_exception(self):
# self.assertRaises(ConsoleException, file_utils.get_file_count, -1)


if __name__ == '__main__':
    unittest.main()
