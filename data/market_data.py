import numpy as np

class MockHyperliquidSDK:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_market_data(self):
        return [{"price": np.random.uniform(25000, 35000), "timestamp": i} for i in range(100)]

    def place_order(self, symbol, size, side):
        print(f"Mock Order Placed: {side} {size} {symbol}")

class MarketDataFetcher:
    def __init__(self, trading_client):
        self.trading_client = trading_client

    def fetch_market_data(self):
        return self.trading_client.get_market_data()

