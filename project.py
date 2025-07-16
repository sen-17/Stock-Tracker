import json
import os
import yfinance 

file_path = "Stock-Tracker\portfolio.json"

def add_stock(ticker , quantity , buy_price):
    if os.path.exists(file_path):
        with open(file_path , mode='r') as file:
            data = json.load(file)
    else:
        data = {}
        with open(file_path , mode="w") as file:
            json.dump(data, file)

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
    pass

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
        except ValueError:
            print("Please input a valid menu.")

if __name__ == "__main__":
    main()