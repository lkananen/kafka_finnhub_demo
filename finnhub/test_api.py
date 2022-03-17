from secrets import API_KEY
import finnhub
import time

def test_stock():
    # Setup client
    finnhub_client = finnhub.Client(api_key=API_KEY)
    
    # Some data sources
    #print(finnhub_client.covid19())
    #print(finnhub_client.fda_calendar())

    # Stock candles
    time_delta_seconds = 60 * 5
    res = finnhub_client.stock_candles('AAPL', 'D', int(time.time() - time_delta_seconds), int(time.time()))
    print(res)
    

def get_symbols(exhange="BINANCE"):
    finnhub_client = finnhub.Client(api_key=API_KEY)
    print(finnhub_client.crypto_symbols(exhange))


if __name__ == "__main__":
    test_stock()
    
    #get_symbols()
