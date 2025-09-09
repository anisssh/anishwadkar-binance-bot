from src.client import BasicBot
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order

def main():
    bot = BasicBot()  # loads keys from .env
    print("Welcome to the Binance Futures Testnet Trading Bot!")

    order_type = input("Enter order type (market/limit): ").strip().lower()
    symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY/SELL): ").strip().upper()
    quantity = float(input("Enter quantity: "))

    if order_type == "market":
        response = place_market_order(bot.client, symbol, side, quantity)
    elif order_type == "limit":
        price = float(input("Enter limit price: "))
        response = place_limit_order(bot.client, symbol, side, quantity, price)
    else:
        print("Invalid order type")
        return

    print("Order response:", response)

if __name__ == "__main__":
    main()
