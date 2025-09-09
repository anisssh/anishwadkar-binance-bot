# import logging

# def place_oco_order(client, symbol, side, quantity, take_profit_price, stop_price, stop_limit_price):
   
#     try:
#         order = client.create_oco_order(
#             symbol=symbol,
#             side=side,
#             quantity=quantity,
#             price=str(take_profit_price),        # Take-profit limit price
#             stopPrice=str(stop_price),           # Stop price for stop-limit
#             stopLimitPrice=str(stop_limit_price),# Limit price for stop-limit
#             stopLimitTimeInForce="GTC"
#         )
#         logging.info(f"OCO order placed: {order}")
#         return order
#     except Exception as e:
#         logging.error(f"Error placing OCO order: {e}")
#         return {"error": str(e)}
