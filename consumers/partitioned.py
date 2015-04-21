#! /usr/bin/env python

"""
Partitioned consumer.

Consumes from one partition, manually specified.
"""
import sys

from kafka import KafkaConsumer

if __name__ == "__main__":
    topic = sys.argv[1]
    partition = int(sys.argv[2])
    consumer = KafkaConsumer((topic, partition),
                             group_id="my_group",
                             metadata_broker_list=["localhost:9092"])

    for message in consumer:
        print "{}:{}:{} {}".format(message.topic,
                                   message.partition,
                                   message.offset,
                                   message.value)
