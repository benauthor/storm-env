#! /usr/bin/env python

"""
Basic round robin producer

Will distribute messages evenly across all the partitions in the topic.

"""
import sys
import time

from kafka import SimpleProducer, KafkaClient

if __name__ == "__main__":

    kafka = KafkaClient("localhost:9092")
    producer = SimpleProducer(kafka)
    topic = sys.argv[1]

    print "Producing messages to topic '{}'".format(topic)

    while True:
        producer.send_messages(topic, "from python at {}".format(time.time()))
        time.sleep(1)
