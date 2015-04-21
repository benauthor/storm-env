# export CLASSPATH=/kafka/libs/*
from jnius import autoclass

# https://cwiki.apache.org/confluence/display/KAFKA/Consumer+Group+Example
ConsumerConfig = autoclass("kafka.consumer.ConsumerConfig")
KafkaStream = autoclass("kafka.consumer.KafkaStream")
ConsumerConnector = autoclass("kafka.javaapi.consumer.ConsumerConnector")

print 'hi'
