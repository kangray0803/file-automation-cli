import argparse

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

args = parser.parse_args()
print(args.command)  #印出指令
print(args.folder)  #印出資料夾路徑