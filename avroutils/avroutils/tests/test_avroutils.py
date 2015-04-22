import avro.schema
import unittest

from avroutils import (
    bulk_deserialize,
    bulk_serialize,
    deserialize,
    serialize,
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

        as_bytes = serialize(some_data, self.schema)
        self.assertIsInstance(as_bytes, basestring)

        back_again = deserialize(as_bytes, self.schema)
        self.assertEqual(back_again['name'], "Lucy")

    def test_bulk_serialize(self):
        some_data = [
            {"name": "Lucy", "favorite_color": "Blue"},
            {"name": "Panda", "favorite_color": "Silver"},
        ]
        as_bytes = bulk_serialize(some_data, self.schema)
        self.assertIsInstance(as_bytes, basestring)

        back_again = bulk_deserialize(as_bytes, self.schema)
        for i, item in enumerate(back_again):
            self.assertEqual(item['name'], some_data[i]['name'])
