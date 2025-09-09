from src.client import BasicBot
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco_order import place_oco_order


def main():
    bot = BasicBot()  # loads keys from .env
    print("Welcome to the Binance Futures Testnet Trading Bot!")

    while True:
        # Select order type
        order_type = input(
            "\nEnter order type (market/limit/stop-limit) or 'exit' to quit: ").strip().lower()
        if order_type == "exit":
            print("Exiting bot. Goodbye!")
            break

        symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
        side = input("Enter side (BUY/SELL): ").strip().upper()
        quantity = float(input("Enter quantity: "))

        # Market order
        if order_type == "market":
            response = place_market_order(bot.client, symbol, side, quantity)

        # Limit order
        elif order_type == "limit":
            price = float(input("Enter limit price: "))
            response = place_limit_order(
                bot.client, symbol, side, quantity, price)

        # Stop-Limit order
        elif order_type == "stop-limit":
            stop_price = float(input("Enter stop price: "))
            limit_price = float(input("Enter limit price: "))
            response = place_stop_limit_order(
                bot.client, symbol, side, quantity, stop_price, limit_price)
        # elif order_type == "oco":
        #     take_profit_price = float(input("Enter take-profit price: "))
        #     stop_price = float(
        #         input("Enter stop price (trigger for stop-limit): "))
        #     stop_limit_price = float(input("Enter stop-limit price: "))
        #     response = place_oco_order(
        #         bot.client, symbol, side, quantity, take_profit_price, stop_price, stop_limit_price)

        else:
            print("Invalid order type")
            continue

        print("Order response:", response)


if __name__ == "__main__":
    main()
