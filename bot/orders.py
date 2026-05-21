def summarize_order(order_response):
    return {
        "orderId": order_response.get("orderId"),
        "status": order_response.get("status"),
        "executedQty": order_response.get("executedQty"),
        "avgPrice": order_response.get("avgPrice", "N/A")
    }
