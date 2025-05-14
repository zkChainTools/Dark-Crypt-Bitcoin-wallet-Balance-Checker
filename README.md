# BTC Wallet Balance Checker (Offline GUI)

This project provides a desktop GUI tool to simulate the checking of Bitcoin wallet balances without internet access.

## Features

- Lightweight graphical interface
- Simulated BTC balance checker
- Result export to .txt
- Encrypted offline scanning module

## Files

- `btc_checker_gui.py` — the main interface
- `btc_core.py` — loader logic for the internal module
- `btc_scanner.data` — encrypted backend scanner module
- `BTC_Checker_Instructions.pdf` — user instructions
- `requirements.txt` — minimal dependency list

## Usage

```bash
pip install -r requirements.txt
python btc_checker_gui.py
```

For Windows 10+ with Python 3.9+.
