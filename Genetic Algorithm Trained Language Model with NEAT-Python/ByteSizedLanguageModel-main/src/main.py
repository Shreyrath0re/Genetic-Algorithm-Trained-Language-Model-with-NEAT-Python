import os
from data import Data
from sentiment_analysis import SentimentAnalyzer  # Import your sentiment analysis module

curr_path = os.getcwd()
file_path = os.path.join(curr_path, "ByteSizedLanguageModel-main", "dataset", "Tweets.csv")
dataset = Data(file_path).data_file

def main():
    text_entry = input("Enter a text entry: ")  # Prompt user for a text entry
    sentiment_value = SentimentAnalyzer.analyze_sentiment(text_entry)  # Use your sentiment analysis model
    print("Sentiment value:", sentiment_value)

if __name__ == "__main__":
    main()
