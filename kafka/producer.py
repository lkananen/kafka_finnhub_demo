from json import dumps
from kafka import KafkaProducer
import websocket
import finnhub
import time


def on_message(ws, message):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    
    producer.send('topic_test', value=message)
    

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AMZN"}')


def run_producer():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.finnhub.io?token=c8l0rlaad3icvur3l0lg",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()


def main():
    run_producer()
    

if __name__ == "__main__":
    main()
