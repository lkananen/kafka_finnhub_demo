# Kafka Docker

## Setup
1. Run `docker-compose -f docker-compose.yml up -d` to start Kafka and Zookeeper.

## Running Kafka producer-consumer
1. Starting the Kafka producer:
   1.1. Connect to the Kafka container:
   `docker exec -it <container-id> /bin/sh`
   1.2. Connect Kafka producer to a topic:
    `kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic test`
2. Starting the Kafka producer:
   2.1. Connect to the Kafka container:
   `docker exec -it <container-id> /bin/sh`
   2.2. Connect Kafka consumer to the same topic :
    `kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic test --from-beginning`
3. Producer can now send messages to the consumer through Kafka.


## Usefull commands
- List running containers `docker ps`
- Stop container `docker stop <container-id>`
- Stop cluster `docker-compose stop`
- Add more brokers `docker-compose scale kafka=3`
