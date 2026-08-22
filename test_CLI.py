import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="檔案管理工具")
parser.add_argument("--folder", required=True, help="要處理的資料夾路徑")
args = parser.parse_args()
print(args.folder)
print(type(args.folder))  # 純文字
folder_path = Path(args.folder)  # 轉換為 Path 物件
print(type(folder_path))  # <class 'pathlib.PosixPath'>