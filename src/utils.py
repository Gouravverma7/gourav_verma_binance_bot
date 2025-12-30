import logging

def setup_logger():
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")
