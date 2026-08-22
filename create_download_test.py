###創建downloads_test###


from pathlib import Path

def create_test_folder():
    test_folder = Path.home() / "Downloads_test"
    test_folder.mkdir(exist_ok=True)

    fake_files = [
        "photo1.jpg", "photo2.png", "screenshot.gif",
        "report.pdf", "notes.docx", "budget.xlsx", "readme.txt",
        "archive.zip", "backup.rar",
        "installer.exe", "setup.msi",
        "data.csv", "config.json",
        "desktop.ini",
        "~$temp_lock.docx",
    ]

    for filename in fake_files:
        file_path = test_folder / filename
        file_path.write_text("測試用假檔案內容")
        print(f"已建立: {filename}")

    print(f"\n測試資料夾位置: {test_folder}")

create_test_folder()