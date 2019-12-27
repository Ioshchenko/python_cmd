import unittest
import utils
from console_exception import ConsoleException


class UtilTestCase(unittest.TestCase):
    def test_should_return_number(self):
        self.assertEqual(utils.get_file_count(0), 0)

    def test_should_throw_exception(self):
        self.assertRaises(ConsoleException, utils.get_file_count, -1)


if __name__ == '__main__':
    unittest.main()
