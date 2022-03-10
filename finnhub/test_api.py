import finnhub
from secrets import API_KEY

# Setup client
finnhub_client = finnhub.Client(api_key=API_KEY)

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)
