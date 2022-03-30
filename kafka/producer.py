from json import dumps
from kafka import KafkaProducer
import websocket
import finnhub
import time
import datetime
import secrets


def on_message(ws: websocket.WebSocketApp, message: str):
    TOPIC_NAME = "topic_test"
    
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    
    producer.send(TOPIC_NAME, value=message)
    print("Message sent - " + str(datetime.datetime.now()) + " - " + str(TOPIC_NAME))
    

def on_error(ws: websocket.WebSocketApp, error: str):
    print(error)


def on_close(ws: websocket.WebSocketApp):
    print("### closed ###")


def on_open(ws: websocket.WebSocketApp):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    #ws.send('{"type":"subscribe","symbol":"AMZN"}')


def run_producer():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.finnhub.io?token=" + secrets.API_KEY,
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
