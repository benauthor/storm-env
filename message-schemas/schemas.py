import avro.schema


def load_schema(path):
    return avro.schema.parse(open(path).read())

demo = load_schema("schemas/demo.json")

__all__ = [
    "demo",
]
