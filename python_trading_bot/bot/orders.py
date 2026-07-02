from .client import BinanceFuturesClient
from .validators import validate_order_input
import logging

def execute_order(symbol, side, order_type, quantity, price=None):
    """Main function to execute trading order"""
    validate_order_input(symbol, side, order_type, quantity, price)
    
    logging.info(f"Order request - {side} {quantity} {symbol} ({order_type}) Price: {price}")
    
    client = BinanceFuturesClient()
    order = client.place_order(symbol, side, order_type, quantity, price)
    
    logging.info(f"Order executed successfully. Order ID: {order.get('orderId')}")
    return order