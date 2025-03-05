from data.market_data import MarketDataFetcher, MockHyperliquidSDK
from data.preprocess import DataPreprocessor
from services.sentiment_analysis import SentimentAnalyzer
from services.trade_execution import TradeExecutor
from models.trading_signals import TradingSignals
from utils.logger import logger

# Initialize components
trading_client = MockHyperliquidSDK()
data_fetcher = MarketDataFetcher(trading_client)
data_preprocessor = DataPreprocessor()
sentiment_analyzer = SentimentAnalyzer()
trade_executor = TradeExecutor(trading_client)

# Fetch market data
logger.info("Fetching market data...")
market_data = data_fetcher.fetch_market_data()
processed_data = data_preprocessor.preprocess(market_data)

# Analyze sentiment
news_article = "Bitcoin surges after major institutional investment."
sentiment = sentiment_analyzer.analyze_sentiment(news_article)
logger.info(f"Sentiment Analysis: {sentiment}")

print("====================================")
print(processed_data)
print("====================================")
# Make a trade decision based on RSI and sentiment
latest_rsi = processed_data.iloc[-1]['RSI']
print(latest_rsi)
trade_signal = TradingSignals.generate_signal(latest_rsi, sentiment['sentiment'])

if trade_signal == "Buy BTC":
    trade_executor.execute_trade("BTC", 1, "buy")
elif trade_signal == "Sell BTC":
    trade_executor.execute_trade("BTC", 1, "sell")
else:
    logger.info("No trade executed based on current conditions.")
