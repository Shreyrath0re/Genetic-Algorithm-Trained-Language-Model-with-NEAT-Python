import os
from data import Data
from sentiment_analysis import SentimentAnalyzer  # Importing sentiment analysis module

# Get dataset path dynamically
curr_path = os.getcwd()
file_path = r"C:\Users\shrey\Downloads\Genetic-Algorithm-Trained-Language-Model-with-NEAT-Python-main\ByteSizedLanguageModel-main\dataset\Tweets.csv"

# Load dataset
dataset = Data(file_path).data_file  # Ensure data.py works correctly

def main():
    text_entry = input("Enter a text entry: ")  # Prompt user for a text entry
    sentiment_value = SentimentAnalyzer.analyze_sentiment(text_entry)  # Use sentiment analysis model
    print(f"Sentiment value: {sentiment_value:.2f}")  # Display result

if __name__ == "__main__":
    main()
