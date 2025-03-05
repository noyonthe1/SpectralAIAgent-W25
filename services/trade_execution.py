class TradeExecutor:
    def __init__(self, trading_client):
        self.trading_client = trading_client

    def execute_trade(self, symbol, size, side):
        try:
            self.trading_client.place_order(symbol, size, side)
            return {"status": "success", "message": f"Trade executed: {side} {size} {symbol}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}