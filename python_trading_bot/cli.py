import argparse
from bot.orders import execute_order
from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logging

def show_price_info(symbol):
    """Display current price and 24h range"""
    try:
        client = BinanceFuturesClient()
        data = client.get_current_price(symbol)
        
        print(f"\nPrice Information for {symbol}:")
        print(f"Current Price : {data['current_price']}")
        print(f"24h High      : {data['high_24h']}")
        print(f"24h Low       : {data['low_24h']}")
    except Exception as e:
        print(f"Could not fetch price information: {e}")

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument('--symbol', type=str, required=True, help='Trading pair (e.g. BTCUSDT)')
    parser.add_argument('--side', type=str, choices=['BUY', 'SELL'], help='BUY or SELL')
    parser.add_argument('--order-type', type=str, choices=['MARKET', 'LIMIT'], help='MARKET or LIMIT')
    parser.add_argument('--quantity', type=float, help='Quantity to trade')
    parser.add_argument('--price', type=float, help='Price for LIMIT order')
    parser.add_argument('--price-info', action='store_true', help='Show current price and 24h range')
    
    args = parser.parse_args()
    
    # Price information only
    if args.price_info:
        show_price_info(args.symbol)
        return
    
    # Order placement
    if not all([args.side, args.order_type, args.quantity]):
        parser.error("Side, order-type and quantity are required for placing orders")
    
    print("\n=== Order Request Summary ===")
    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Type        : {args.order_type}")
    print(f"Quantity    : {args.quantity}")
    if args.price:
        print(f"Price       : {args.price}")
    
    try:
        order = execute_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )
        
        print("\n=== Order Response ===")
        print(f"Order ID       : {order.get('orderId')}")
        print(f"Status         : {order.get('status')}")
        print(f"Executed Qty   : {order.get('executedQty')}")
        if order.get('avgPrice'):
            print(f"Average Price  : {order.get('avgPrice')}")
        print("Success: Order placed successfully on Testnet.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()