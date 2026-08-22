# File Automation CLI

一個簡單的檔案管理命令列工具，可以自動整理下載資料夾、批次重新命名檔案、備份資料夾。

## 功能

- **organize**：依副檔名自動分類搬移檔案（圖片 / 文件 / 壓縮檔 / 安裝檔 / 其他），並自動跳過系統檔（如 desktop.ini）與 Office 暫存鎖定檔
- **rename**：批次重新命名，支援三種規則
  - `number`：加流水號，例如 `photo_001.jpg`
  - `date`：加日期＋流水號，例如 `photo_2026-08-02_001.jpg`
  - `prefix`：保留原檔名，只加前綴，例如 `vacation_IMG_0001.jpg`
- **backup**：將整個資料夾複製一份，並自動加上日期標記

## 環境需求

- Python 3.10+
- 無需安裝額外套件（僅使用內建的 `pathlib`、`shutil`、`argparse`、`datetime`）

## 使用方式

### 整理資料夾

```bash
python full_program.py organize --folder "C:\Users\user\Downloads_test"
```

### 批次重新命名

```bash
python full_program.py rename --folder "C:\Users\user\Downloads\圖片" --style prefix --prefix vacation
python full_program.py rename --folder "C:\Users\user\Downloads\文件" --style number --prefix report
python full_program.py rename --folder "C:\Users\user\Downloads\安裝檔" --style date --prefix setup
```

`--style` 只能選 `number`、`date`、`prefix` 其中一種，`--prefix` 為必填參數。

### 備份資料夾

```bash
python full_program.py backup --folder "C:\Users\user\Downloads_test"
```
