import unittest
import schema


class SchemaTestCase(unittest.TestCase):
    def test_should_create_data(self):
        data = '{"date":"timestamp:", "name": "str:rand", "type":"str:[\'client\', \'partner\', \'government\']", "age": "int:rand(1, 90)"}'
        result = schema.generate(data, 1)
        self.assertEqual(len(result), 1)
