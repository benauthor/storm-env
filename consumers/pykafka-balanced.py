#! /usr/bin/env python
"""
Trying out pykafka balanced consumer.

"""
import sys
import time

from pykafka import KafkaClient

if __name__ == "__main__":
    topic_name = sys.argv[1]
    try:
        group_name = sys.argv[2]
    except IndexError:
        group_name = "default"
    client = KafkaClient(hosts='localhost:9092')
    topic = client.topics.get(topic_name)
    if not topic:
        print "no topic %s" % topic_name
        sys.exit(1)

    consumer = topic.get_balanced_consumer(consumer_group=group_name)

    while True:
        message = consumer.consume()
        print "{}:{}:{}".format(message.partition_key,
                                message.offset,
                                message.value)
