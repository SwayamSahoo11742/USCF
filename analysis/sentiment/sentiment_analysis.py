from textblob import TextBlob

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
