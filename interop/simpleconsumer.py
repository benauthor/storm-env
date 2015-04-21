# export CLASSPATH=/kafka/libs/*
from jnius import autoclass

SimpleConsumer = autoclass("kafka.javaapi.consumer.SimpleConsumer")

consumer = SimpleConsumer("localhost", 9092, 10000, 1024000, "my-consumer")

# gets hairy here. High level consumer is probably easier.
