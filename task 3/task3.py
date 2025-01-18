import requests

API_KEY = 'your_alpha_vantage_api_key'  # Replace with your Alpha Vantage API key
BASE_URL = 'https://www.alphavantage.co/query?'

# Portfolio class to manage stock data
class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, price_per_share):
        if symbol not in self.stocks:
            self.stocks[symbol] = {'quantity': quantity, 'price_per_share': price_per_share}
        else:
            self.stocks[symbol]['quantity'] += quantity
        print(f"Added {quantity} shares of {symbol} at ${price_per_share} each.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks and self.stocks[symbol]['quantity'] >= quantity:
            self.stocks[symbol]['quantity'] -= quantity
            if self.stocks[symbol]['quantity'] == 0:
                del self.stocks[symbol]
            print(f"Removed {quantity} shares of {symbol}.")
        else:
            print(f"Not enough shares to remove or stock not found.")

    def get_stock_value(self, symbol):
        stock_info = self.stocks.get(symbol)
        if stock_info:
            current_price = self.get_current_price(symbol)
            total_value = stock_info['quantity'] * current_price
            return total_value, current_price
        else:
            return 0, 0

    def get_current_price(self, symbol):
        url = f"{BASE_URL}function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if 'Time Series (5min)' in data:
            last_refreshed = list(data['Time Series (5min)'].keys())[0]
            latest_data = data['Time Series (5min)'][last_refreshed]
            current_price = float(latest_data['4. close'])
            return current_price
        else:
            print("Error fetching stock data.")
            return 0

    def track_portfolio(self):
        total_value = 0
        print("\nStock Portfolio Performance:")
        for symbol, details in self.stocks.items():
            total_value_stock, current_price = self.get_stock_value(symbol)
            total_value += total_value_stock
            print(f"{symbol}: {details['quantity']} shares at ${current_price:.2f} each. Total value: ${total_value_stock:.2f}")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")


def main():
    portfolio = StockPortfolio()

    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity of shares: "))
            price_per_share = float(input("Enter purchase price per share: "))
            portfolio.add_stock(symbol, quantity, price_per_share)

        elif choice == '2':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity of shares to remove: "))
            portfolio.remove_stock(symbol, quantity)

        elif choice == '3':
            portfolio.track_portfolio()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
