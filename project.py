import json
import os
import yfinance
from tabulate import tabulate

file_path = "Stock-Tracker\portfolio.json"

def add_stock(ticker , quantity , buy_price):
    if os.path.exists(file_path):
        with open(file_path , mode='r') as file:
            data = json.load(file)
    else:
        data = {}
        with open(file_path , mode="w") as file:
            json.dump(data, file)

    ticker = ticker.upper()
    data[ticker] = {"quantity" : quantity , "buy_price": buy_price}
    with open(file_path , "w") as file:
        json.dump(data, file , indent = 2)

    return data

def get_live_price(ticker):
    try:
        stock = yfinance.Ticker(ticker)
        last_price = stock.fast_info['last_price']
        return last_price
    except Exception as e:
        print(f"Error getting price for {ticker}: {e}")
        return None

def calculate_portfolio_value():
    total_value = 0
    total_gain_loss = 0
    all_data = [["Ticker", "Quantity", "Buy Price", "Current Price", "Gain/Loss"]]
    with open(file_path , mode="r") as file:
        data = json.load(file)
        
        for (key,value) in data.items():
            stock_quantity = value["quantity"]
            stock_buy_price = value["buy_price"]
            stock_live_price = get_live_price(key)

            if get_live_price is None:
                continue

            total = stock_quantity * stock_live_price
            total_value += total
            gain_loss = (stock_live_price - stock_buy_price) * stock_quantity
            total_gain_loss += gain_loss

            all_data.append([
                key,
                stock_quantity,
                f"${stock_buy_price:.2f}",
                f"${stock_live_price:.2f}",
                f"${gain_loss:.2f}"
            ])

    print(tabulate(all_data , headers = "firstrow", tablefmt="grid"))
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    print(f"Total Gain\Loss: {total_gain_loss:+.2f}")
        

def main():
    while True:
        print("==== Stock Portfolio Tracker ====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        user_input = int(input("Choose an option: "))

        try:
            if user_input == 1:
                ticker = input("Enter stock ticker (e.g., AAPL): ")
                quantity = int(input("Quantity: "))
                buy_price = float(input("Buy price: "))
                add_stock(ticker , quantity, buy_price)

            elif user_input == 2:
                calculate_portfolio_value()

            elif user_input == 3:
                print("Exiting the program...")
                break
        except ValueError:
            print("Please input a valid menu.")

if __name__ == "__main__":
    main()