import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        base_url = "https://testnet.binancefuture.com" if testnet else None
        self.client = Client(api_key, api_secret, testnet=testnet)
        if base_url:
            self.client.FUTURES_URL = base_url

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Order placed: {order}")
            return order

        except BinanceAPIException as e:
            logging.error(f"API Error: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            raise
