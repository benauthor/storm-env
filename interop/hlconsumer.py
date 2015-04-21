#!/usr/bin/env python

# export CLASSPATH=/kafka/libs/* && ./hlconsumer.py test

# bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 4 --topic test

import sys

from jnius import autoclass

# https://cwiki.apache.org/confluence/display/KAFKA/Consumer+Group+Example
Consumer = autoclass("kafka.consumer.Consumer")
ConsumerConfig = autoclass("kafka.consumer.ConsumerConfig")
KafkaStream = autoclass("kafka.consumer.KafkaStream")
ConsumerConnector = autoclass("kafka.javaapi.consumer.ConsumerConnector")

Properties = autoclass("java.util.Properties")
HashMap = autoclass("java.util.HashMap")
Integer = autoclass("java.lang.Integer")


def create_consumer_config(a_zookeeper, a_group_id):
    props = Properties()
    props.put("zookeeper.connect", a_zookeeper)
    props.put("group.id", a_group_id)
    props.put("zookeeper.session.timeout.ms", "400")
    props.put("zookeeper.sync.time.ms", "200")
    props.put("auto.commit.interval.ms", "1000")
    return ConsumerConfig(props)


def create_consumer(config):
    return Consumer.createJavaConsumerConnector(config)


if __name__ == "__main__":

    topic = sys.argv[1]
    config = create_consumer_config("localhost:2181", "test-group")
    consumer = create_consumer(config)

    # simple topic map: a single stream for the topic
    topics_map = HashMap()
    topics_map.put(topic, Integer(1))

    # get my single stream out of the consumer
    consumer_map = consumer.createMessageStreams(topics_map)
    streams = consumer_map.get(topic)
    stream = streams.get(0)
    it = stream.iterator()

    while it.hasNext():
        msg = it.next()
        mt = msg.topic()
        mp = msg.partition()

        print "{}:{}:{} {}".format(msg.topic(),
                                   msg.partition(),
                                   msg.offset(),
                                   msg.message().tostring())
