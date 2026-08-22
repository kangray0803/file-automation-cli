import argparse
from pathlib import Path
from file_tools import (
    organize_downloads,
    rename_with_number,
    rename_with_date,
    rename_with_prefix,
    backup_folder2,
)

from stock_tools import (
    get_stock_info,
    check_price_alert
)

parser = argparse.ArgumentParser(description="檔案管理工具")
subparsers = parser.add_subparsers(dest="command", required=True)

# 定義 organize 子命令
organize_parser = subparsers.add_parser("organize", help="整理資料夾")
organize_parser.add_argument("--folder", required=True, help="要整理的資料夾")

# 定義 backup 子命令
backup_parser = subparsers.add_parser("backup", help="備份資料夾")
backup_parser.add_argument("--folder", required=True, help="要備份的資料夾")

# 定義 rename 子命令
rename_parser = subparsers.add_parser("rename", help="批次重新命名")
rename_parser.add_argument("--folder", required=True, help="要重新命名的資料夾")
rename_parser.add_argument("--style", required=True, choices=["number", "date", "prefix"], help="命名規則")
rename_parser.add_argument("--prefix", required=True, help="檔案前綴文字")

# 定義 stock_info 子命令
stock_parser = subparsers.add_parser("stock_info", help="獲取股票資訊")
stock_parser.add_argument("--ticker", required=True, help="股票代碼")

# 定義 check_price_alert 子命令
alert_parser = subparsers.add_parser("alert", help="檢查價格警報")
alert_parser.add_argument("--ticker", required=True, help="股票代碼")
alert_parser.add_argument("--threshold", required=True, type=float, help="價格閾值")
alert_parser.add_argument("--direction", required=True, choices=["above", "below"], help="價格方向")

args = parser.parse_args()
# folder_path = Path(args.folder)

if args.command == "organize":
    organize_downloads(Path(args.folder))
elif args.command == "backup":
    backup_folder2(Path(args.folder))
elif args.command == "rename":
    if args.style == "number":
        rename_with_number(Path(args.folder), args.prefix)
    elif args.style == "date":
        rename_with_date(Path(args.folder), args.prefix)
    elif args.style == "prefix":
        rename_with_prefix(Path(args.folder), args.prefix)
elif args.command == "stock_info":
    stock_info = get_stock_info(args.ticker)
    print(f"股票代碼: {args.ticker}")
    print(f"當前價格: {stock_info['currentPrice']}")
    print(f"前一日收盤價: {stock_info['previousClose']}")
    print(f"價格變動: {stock_info['change']}")
    print(f"價格變動百分比: {stock_info['changePercent']:.2f}%")
elif args.command == "alert":
    result = check_price_alert(args.ticker, args.threshold, args.direction)
    if result:
        print(f"警報: 股票 {args.ticker} 的價格已經 {'高於' if args.direction == 'above' else '低於'} {args.threshold}")
    else:
        print(f"提示: 股票 {args.ticker} 的價格尚未 {'高於' if args.direction == 'above' else '低於'} {args.threshold}")