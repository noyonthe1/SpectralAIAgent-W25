
class TradingSignals:
    @staticmethod
    def generate_signal(rsi, sentiment):
        print(sentiment)
        if rsi < 30 and sentiment == "positive":
            return "Buy BTC"
        elif rsi > 70 and sentiment == "negative":
            return "Sell BTC"
        return "Hold"