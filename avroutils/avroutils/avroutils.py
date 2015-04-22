import io
import avro.schema
import avro.io


def serialize(data_structure, schema):
    writer = avro.io.DatumWriter(writers_schema=schema)
    out = io.BytesIO()
    writer.write(data_structure, avro.io.BinaryEncoder(out))
    return out.getvalue()


def bulk_serialize(data_structures, schema):
    writer = avro.io.DatumWriter(writers_schema=schema)
    out = io.BytesIO()
    encoder = avro.io.BinaryEncoder(out)
    for data_structure in data_structures:
        writer.write(data_structure, encoder)
    return out.getvalue()


def deserialize(as_bytes, schema):
    bytes_reader = io.BytesIO(as_bytes)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(writers_schema=schema)
    return reader.read(decoder)


def bulk_deserialize(as_bytes, schema):
    bytes_reader = io.BytesIO(as_bytes)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(writers_schema=schema)
    while True:
        try:
            yield reader.read(decoder)
        except TypeError:
            raise StopIteration
