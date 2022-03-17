# Kafka Docker

## Setup
1. Run `docker-compose up -d` to start Kafka and Zookeeper.

## Running Kafka producer-consumer
1. Connect to the Kafka container:
   `docker exec -it <container-id> /bin/sh`
2. Connect Kafka producer to a topic:
    `kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic test`
3. Connect Kafka consumer to the same topic :
    `kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic test --from-beginning`
4. Producer can now send messages to the consumer through Kafka.


## Usage tips
- list running processes `docker ps`
- stop processes `docker stop ID`

## Source
- https://hub.docker.com/r/bitnami/kafka/
- https://github.com/bitnami/bitnami-docker-kafka
