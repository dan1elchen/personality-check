from nltk.sentiment import SentimentIntensityAnalyzer

def popularityScore(text):
    sia = SentimentIntensityAnalyzer()
    popularity = sia.polarity_scores(text)
    return popularity
    