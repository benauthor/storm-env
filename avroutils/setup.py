from distutils.core import setup

setup(
    name='avroutils',
    version='0.1',
    description='Utilities for serializing to Avro',
    author='Evan Bender',
    author_email='evan.bender@percolate.com',
    packages=['avroutils'],
    install_requires=['avro'],
)
