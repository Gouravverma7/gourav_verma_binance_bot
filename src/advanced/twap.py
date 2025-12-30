import time

def twap_order(symbol, side, total_qty, chunks, interval):
    qty_per_order = total_qty / chunks

    for i in range(chunks):
        client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty_per_order
        )
        time.sleep(interval)
