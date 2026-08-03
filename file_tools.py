import os  # 讀取資料夾、判斷路徑
import shutil  # 搬移檔案
from pathlib import Path  # 更方便的路徑操作方式
from datetime import datetime, date

IGNORE_FILES = {"desktop.ini", "thumbs.db"}
CATEGORIES = {
    "圖片": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "文件": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "壓縮檔": [".zip", ".rar", ".7z"],
    "安裝檔": [".exe", ".msi"],
}
def get_category(extension):
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "其他"

# 移動檔案到對應的資料夾
# download_folder=Path.home() / "Downloads_test"
def organize_downloads(folder_path):
    for item in folder_path.iterdir():
        if item.name.startswith("~$") or item.name in IGNORE_FILES:
            continue
        if item.is_file():
            category = get_category(item.suffix)
            target_folder = folder_path / category
            target_folder.mkdir(exist_ok=True)

            target_path = target_folder / item.name
            shutil.move(str(item), str(target_path))
            print(f"Moving {item.name} to {category}")

# organize_downloads(download_folder)






# 加上流水號在檔名中
# download_document_file=Path.home() / "Downloads_test/文件"
def rename_with_number(folder_path, prefix):
    counter = 1
    for item in folder_path.iterdir():
        if item.is_file():
            new_name = f"{prefix}_{counter:03d}{item.suffix}"
            counter += 1
            item.rename(folder_path / new_name)
            
# rename_with_number(download_document_file, "文件")


# 取得今天日期在檔名中
# today=date.today()
# print(f"今天日期: {today}")

# download_installation_file=Path.home() / "Downloads_test/安裝檔"
def rename_with_date(folder_path, prefix):
    today=date.today()
    counter = 0
    for item in folder_path.iterdir():
        if item.is_file():
            counter += 1
            new_name = f"{prefix}_{today}_{counter:03d}{item.suffix}"
            item.rename(folder_path / new_name)

# rename_with_date(download_installation_file, "安裝檔")




# 加入前綴文字在檔名中
# download_photo_file=Path.home() / "Downloads_test/圖片"
def rename_with_prefix(folder_path, prefix):
    for item in folder_path.iterdir():
        if item.is_file():
            new_name = f"{prefix}_{item.name}"
            item.rename(folder_path / new_name)

# rename_with_prefix(download_photo_file, "vacation")




#備份
# target_folder = Path.home() / "Downloads_test"
# def backup_folder(source_folder):
#     for item in source_folder.iterdir():
#         if item.is_dir():
#             shutil.copytree(source_folder / item.name, f"{source_folder / item.name}_{today}_backup")
    
# backup_folder(target_folder)




#備份
# target_folder2 = Path.home() / "Downloads_test"
def backup_folder2(source_folder):
    today=date.today()
    shutil.copytree(source_folder, f"{source_folder}_{today}_backup")
    
# backup_folder2(target_folder2)