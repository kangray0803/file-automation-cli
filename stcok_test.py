import yfinance as yf

# stock = yf.Ticker("2330.TW")
# print(stock.info["currentPrice"])

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    curr_price = stock.info["currentPrice"]
    prev_close = stock.info["previousClose"]
    
    return {
        "currentPrice": curr_price,
        "previousClose": prev_close,
        "change": curr_price - prev_close,
        "changePercent": ((curr_price - prev_close) / prev_close * 100) if prev_close != 0 else 0
    }

print(get_stock_info("2330.TW"))