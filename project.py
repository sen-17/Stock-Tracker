import json
import os

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
    pass

def calculate_portfolio_value():
    pass

def main():
    while True:
        print("==== Stock Portfolio Tracker ====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        user_input = int(input("Choose an option: "))

        if user_input == 1:
            ticker = input("Enter stock ticker (e.g., AAPL): ")
            quantity = int(input("Quantity: "))
            buy_price = float(input("Buy price: "))
            add_stock(ticker , quantity, buy_price)

        elif user_input == 2:
            calculate_portfolio_value()

if __name__ == "__main__":
    main()