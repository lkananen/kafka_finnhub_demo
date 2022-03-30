# Kafka
Topic producer and consumer scripts.

## Producer - Consumer model
Kafka platform handles and stores event data through two types of clients: a producer and a consumer. Producer client applications writes events to Kafka and consumers read and processess those events.

### Producer
Producer connects a source, in this case a websocket, to a registered Kafka topic and publishes information to the topic. Websocket information flows to the topic as a data stream and gets stored to Kafka.

Flow chart:
```
API -> Websocket -> Producer -> Kafka topic -> Kafka
```

### Consumer
Consumer subscribes to listen to the content of a topic. Topic content can be listened as a real-time stream and/or it can be played back from some timepoint to access previous data. This allows data processing as the events occur or retrospectively.

Flow chart:
```
Kafka -> Kafka topic -> Consumer
```

### Topic
Topics are the Kafka storage units of certain events. They are partitioned across brokers to make the read/write access to the data more scalable and allowing multiple brokers to run simultaneously.


## More details:
- https://kafka.apache.org/intro
