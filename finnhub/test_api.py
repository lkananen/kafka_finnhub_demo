from secrets import API_KEY
import finnhub
import time
import websocket


##############################################################################
# Stock market data

def test_stock():
    # Setup client
    finnhub_client = finnhub.Client(api_key=API_KEY)
    
    # Some data sources
    #print(finnhub_client.covid19())
    #print(finnhub_client.fda_calendar())

    # Stock candles
    time_delta_seconds = 60*5
    res = finnhub_client.stock_candles('AAPL', 'D', int(time.time() - time_delta_seconds), int(time.time()))
    print(res)


##############################################################################
# Websocket

def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


def test_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c8l0rlaad3icvur3l0lg",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

##############################################################################


if __name__ == "__main__":
    test_websocket()
