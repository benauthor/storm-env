#! /usr/bin/env python
"""
Dumb partition-unaware consumer.

Consumes everything from the topic.

"""
import sys

from pykafka import KafkaClient

if __name__ == "__main__":
    topic_name = sys.argv[1]
    client = KafkaClient(hosts='localhost:9092')
    topic = client.topics.get(topic_name)
    if not topic:
        print "no topic %s" % topic_name
        sys.exit(1)

    consumer = topic.get_simple_consumer()

    for message in consumer:
        if message:
            print "{}:{}:{}".format(message.partition_key,
                                    message.offset,
                                    message.value)
