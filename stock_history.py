import csv


with open("stock_history.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["2330.TW", "2026-08-30", "2440.0"])