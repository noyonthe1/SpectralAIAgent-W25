import openai
import json
from config import OPENAI_API_KEY
from utils.logger import logger

class SentimentAnalyzer:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def analyze_sentiment(self, news_article):
        try:
            # Request sentiment analysis
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a financial sentiment analysis assistant."},
                    {"role": "user", "content": f"Analyze this news article: {news_article}. Return a valid JSON format using double quotes: {{\"sentiment\": \"positive\", \"reason\": \"Your reasoning here\"}}."}
                ],
                max_tokens=1000
            )

            # Extract the content
            raw_content = response["choices"][0]["message"]["content"]
            print("Received content:", raw_content)

            try:
                # Attempt JSON parsing
                sentiment_data = json.loads(raw_content)
                print("Parsed sentiment data:", sentiment_data)
                return sentiment_data
            except json.JSONDecodeError as json_error:
                logger.error(f"Failed to parse JSON: {json_error}")
                logger.error(f"Raw response: {raw_content}")  # Log the problematic response
                return {"sentiment": "neutral", "reason": "Error processing sentiment analysis"}

        except Exception as e:
            logger.error(f"Sentiment analysis failed: {e}")
            return {"sentiment": "neutral", "reason": "Error processing sentiment analysis"}
