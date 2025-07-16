# Stock-Tracker

# CLI Stock Portfolio Tracker

#### Video Demo: [Watch the video on YouTube](https://youtu.be/YOfrgxBejiY)
#### Description:
This is a Final Project for CS50p, i built a command-line tool that helps users track and monitor a stock portfolio by adding stock tickers, quantities, and purchase prices. It fetches **live stock prices** using Yahoo Finance (via `yfinance`) and calculates:

- Current value of each stock
- Total portfolio value
- Profit/loss per stock and overall

### Features
- Add stocks with buy price and quantity
- Real-time stock price lookup
- Gain/loss calculation
- Terminal table output (with `tabulate`)
- JSON-based persistent storage

### Files
- `project.py` — main program file containing all core logic
- `test_project.py` — contains unit tests using `pytest` and mocks
- `portfolio.json` — stores user’s portfolio data
- `requirements.txt` — dependencies (`yfinance`, `tabulate`)

### Technologies
- Python 3
- `yfinance`
- `tabulate`
- `json`, `os`
- `pytest`, for testing

### Design Decisions
- I used JSON for persistence because it's simple and readable.
- I chose `tabulate` for clean CLI output without needing external GUI.
- I implemented error handling for ticker lookup and invalid input.
- Uppercased tickers to normalize user input.

### How to Run
1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the tracker:
    ```bash
    python project.py
    ```

3. Run tests:
    ```bash
    pytest test_project.py
    ```
