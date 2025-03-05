import pandas as pd

class DataPreprocessor:
    @staticmethod
    def calculate_rsi(prices, period=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def preprocess(self, market_data):
        df = pd.DataFrame(market_data)
        df['MA_50'] = df['price'].rolling(window=50).mean()
        df['RSI'] = self.calculate_rsi(df['price'])
        df.fillna(0, inplace=True)
        return df