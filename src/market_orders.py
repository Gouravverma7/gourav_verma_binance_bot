import sys
import logging
from client import BasicBot
from utils import setup_logger, validate_side, validate_quantity

setup_logger()

def place_market_order(symbol, side, quantity):
    validate_side(side)
    validate_quantity(quantity)

    bot = BasicBot("API_KEY", "API_SECRET")
    client = bot.get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order Success: {order}")
        print(order)
    except Exception as e:
        logging.error(str(e))
        print("Error:", e)

if __name__ == "__main__":
    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])

    place_market_order(symbol, side, quantity)
