from kafka import KafkaConsumer
import json
import time
import datetime


def run_consumer():
    global VALUE_BUFFER
    
    consumer = KafkaConsumer(
        'topic_test',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-id',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("Messages read - " + str(datetime.datetime.now()))

    for event in consumer:
        event_data = event.value
        
        values = [val["p"] for val in json.loads(event_data)["data"]]
        print(values)
        
        time.sleep(0.5)

        
def main():
    run_consumer()
    

if __name__ == "__main__":
    main()
