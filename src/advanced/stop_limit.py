import logging


def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    ticker = client.futures_symbol_ticker(symbol=symbol)
    current_price = float(ticker['price'])

    if side.upper() == "SELL" and stop_price <= current_price:
        return {"error": "Stop price must be above current market price for SELL"}
    if side.upper() == "BUY" and stop_price >= current_price:
        return {"error": "Stop price must be below current market price for BUY"}

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            type="STOP",
            stopPrice=stop_price,
            price=limit_price,
            timeInForce="GTC"
        )
        logging.info("stop limit order placed", order)
        return order
    except Exception as e:
        logging.exception("Error in stop_limit order {e} ")
        return {"error", str(e)}
    
