import yfinance as yf
from datetime import datetime
import csv
from pathlib import Path

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
    
def save_stock_history(ticker, price):
    csv_path = Path(__file__).parent / "stock_history.csv"
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ticker, timestamp, price])