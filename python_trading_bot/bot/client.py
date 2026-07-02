from binance import Client
import os
from dotenv import load_dotenv
import logging

load_dotenv()

class BinanceFuturesClient:
    """Wrapper for Binance Futures Testnet API"""
    
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not api_key or not api_secret:
            raise Exception("API keys not found in .env file")
        
        self.client = Client(api_key, api_secret, testnet=True)
        logging.info("Successfully connected to Binance Futures Testnet")
    
    def place_order(self, symbol, side, order_type, quantity, price=None):
        """Place market or limit order"""
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }
            
            if order_type == "LIMIT" and price:
                params["price"] = price
                params["timeInForce"] = "GTC"
            
            order = self.client.futures_create_order(**params)
            return order
        except Exception as e:
            logging.error(f"Failed to place order: {e}")
            raise
    
    def get_current_price(self, symbol: str):
        """Get current price, day's high and low"""
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            current_price = float(ticker['lastPrice'])
            
            # Get 24h statistics
            stats = self.client.futures_ticker(symbol=symbol)
            high = float(stats['highPrice'])
            low = float(stats['lowPrice'])
            
            return {
                "current_price": current_price,
                "high_24h": high,
                "low_24h": low
            }
        except Exception as e:
            logging.error(f"Failed to fetch price data: {e}")
            raise