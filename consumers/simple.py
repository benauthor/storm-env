#! /usr/bin/env python

"""
Dumb partition-unaware consumer.

Consumes everything from the topic.

"""
import sys

from kafka import KafkaConsumer

if __name__ == "__main__":
    topic = sys.argv[1]
    consumer = KafkaConsumer(topic,
                             group_id="my_group",
                             metadata_broker_list=["localhost:9092"])

    for message in consumer:
        print "{}:{}:{} {}".format(message.topic,
                                   message.partition,
                                   message.offset,
                                   message.value)
