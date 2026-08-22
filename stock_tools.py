import yfinance as yf

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

def check_price_alert(ticker, threshold, direction):
    stock_info = get_stock_info(ticker)
    curr_price = stock_info["currentPrice"]
    
    if direction == "above":
        return curr_price > threshold
    elif direction == "below":
        return curr_price < threshold