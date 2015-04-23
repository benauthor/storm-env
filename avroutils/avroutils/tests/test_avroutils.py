import avro.schema
import unittest

from avroutils import (
    deserialize,
    serialize,
    serialize_one,
)


TEST_SCHEMA_JSON = '''
{
"namespace": "example.avro",
 "type": "record",
 "name": "User",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": ["int", "null"]},
     {"name": "favorite_color", "type": ["string", "null"]}
 ]
}
'''


class TestSerialize(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.schema = avro.schema.parse(TEST_SCHEMA_JSON)

    def test_serialize_roundtrip(self):
        some_data = {"name": "Lucy", "favorite_color": "Blue"}

        as_bytes = serialize_one(some_data, self.schema)
        self.assertIsInstance(as_bytes, basestring)
        self.assertGreater(len(as_bytes), 1)

        back_again = deserialize(as_bytes).next()
        self.assertEqual(back_again['name'], "Lucy")

    def test_bulk_serialize(self):
        some_data = [
            {"name": "Lucy", "favorite_color": "Blue"},
            {"name": "Linus", "favorite_color": "Silver"},
            {"name": "Snoopy", "favorite_number": 1},
        ]
        as_bytes = serialize(some_data, self.schema)
        self.assertIsInstance(as_bytes, basestring)
        self.assertGreater(len(as_bytes), 1)

        back_again = deserialize(as_bytes)
        for i, item in enumerate(back_again):
            self.assertEqual(item['name'], some_data[i]['name'])
