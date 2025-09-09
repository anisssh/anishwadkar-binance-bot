# """
# twap.py - simple TWAP skeleton
# """
# import time
# def twap_execute(place_order_func, symbol, side, total_qty, slices=5, interval_secs=60):
#     per_slice = total_qty / slices
#     results = []
#     for i in range(slices):
#         res = place_order_func(symbol=symbol, side=side, quantity=per_slice)
#         results.append(res)
#         time.sleep(interval_secs)
#     return results
