from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# Function to analyze sentiment
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        sentiment = "Positive"
    elif score['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, score


# Example usage
if __name__ == "__main__":
    texts = [
        "I am angry."
    ]

    for text in texts:
        sentiment, score = analyze_sentiment(text)
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}")
        print(f"Score: {score}")
        print("-" * 50)
