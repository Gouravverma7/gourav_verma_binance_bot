def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logging.info(f"Limit Order Placed: {order}")
        print(order)
    except Exception as e:
        logging.error(e)
