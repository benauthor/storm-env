import io
import avro.datafile
import avro.io
import avro.schema


def serialize(data, schema):
    datum_writer = avro.io.DatumWriter(writers_schema=schema)
    out = io.BytesIO()
    writer = avro.datafile.DataFileWriter(out, datum_writer, schema)
    for datum in data:
        writer.append(datum)
    writer.flush()
    return out.getvalue()


def serialize_one(datum, schema):
    return serialize([datum], schema)


def deserialize(as_bytes):
    bytes_in = io.BytesIO(as_bytes)
    datum_reader = avro.io.DatumReader()
    reader = avro.datafile.DataFileReader(bytes_in, datum_reader)
    for datum in reader:
        yield datum
