def validate_order_input(symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> bool:
    """Validate all user inputs before placing an order"""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol is required (example: BTCUSDT)")
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL")
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price is required and must be greater than zero for LIMIT orders")
    return True