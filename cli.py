import argparse
from bot.client import BinanceFuturesClient
from bot.orders import summarize_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")
    args = parser.parse_args()

    validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

    client = BinanceFuturesClient(api_key="9ROktThsU8n5pUHvxNBfMcEZnRVcqjtKsCTS2pFZOMLU1pUuG5fwP5jVVQBPHsye", api_secret="EHwzMVrcM6FGPwaKU0NhJcZIHuG4pxlf1jWH7ehR2CcR83NdcniBELRyfQR6WIe4")
    order_response = client.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    summary = summarize_order(order_response)
    print("Order Summary:", summary)

if __name__ == "__main__":
    main()
