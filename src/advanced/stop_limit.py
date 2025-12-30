def stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="STOP",
        quantity=quantity,
        stopPrice=stop_price,
        price=limit_price,
        timeInForce="GTC"
    )
    return order
