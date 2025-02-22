from textblob import TextBlob  # Using TextBlob for simple sentiment analysis

class SentimentAnalyzer:
    @staticmethod
    def analyze_sentiment(text):
        """Analyzes sentiment and returns a score (-1 to 1)."""
        analysis = TextBlob(text).sentiment
        return analysis.polarity  # Returns sentiment polarity (-1 = Negative, 1 = Positive)
