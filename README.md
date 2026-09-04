# File Automation CLI

一個簡單的命令列工具，整合檔案管理與股票查詢功能，包含自動整理下載資料夾、批次重新命名檔案、備份資料夾，以及股票即時查詢與價格警報。

## 功能

- **organize**：依副檔名自動分類搬移檔案（圖片 / 文件 / 壓縮檔 / 安裝檔 / 其他），並自動跳過系統檔（如 desktop.ini）與 Office 暫存鎖定檔
- **rename**：批次重新命名，支援三種規則
  - `number`：加流水號，例如 `photo_001.jpg`
  - `date`：加日期＋流水號，例如 `photo_2026-08-02_001.jpg`
  - `prefix`：保留原檔名，只加前綴，例如 `vacation_IMG_0001.jpg`
- **backup**：將整個資料夾複製一份，並自動加上日期標記

### 股票查詢

- **stock_info**：查詢股票即時資訊，包含目前股價、前一日收盤價、漲跌金額與漲跌幅
- **alert**：設定價格門檻，檢查股價是否已漲破/跌破指定價位

## 環境需求

- Python 3.10+
- 無需安裝額外套件（僅使用內建的 `pathlib`、`shutil`、`argparse`、`datetime`）
```bash
  pip install yfinance
```
- 其餘皆為 Python 內建模組（`pathlib`、`shutil`、`argparse`、`datetime`）

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

### 查詢股票資訊

```bash
python full_program.py stock_info --ticker 2330.TW
```

### 股價警報

```bash
python full_program.py alert --ticker 2330.TW --threshold 1000 --direction below
python full_program.py alert --ticker 2330.TW --threshold 1100 --direction above
```

`--direction` 只能選 `above`（漲破）或 `below`（跌破）。

## 注意事項

- `rename` 系列功能是**破壞性操作**（原檔名會被直接覆蓋），建議先在測試資料夾練習，確認結果符合預期後再用於正式檔案
- `organize` 執行前建議先確認目標資料夾內容，避免誤搬重要檔案
- 股票資料透過 `yfinance` 取得，存在約 15–20 分鐘的延遲，不適合用於高頻交易情境
