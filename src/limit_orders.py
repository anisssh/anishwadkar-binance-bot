import logging


def place_limit_order(client, symbol, side, quantity, price):
    """Place a futures limit order."""
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logging.info(f"Limit order placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Error placing limit order: {e}")
        return {"error": str(e)}
