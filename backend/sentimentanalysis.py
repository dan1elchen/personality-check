from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Blueprint

sentimentAnalysis = Blueprint("sentimentAnalysis", __name__)

@sentimentAnalysis.route("/get-popularity-score")
def getPopularityScore(text):
    sia = SentimentIntensityAnalyzer()
    popularity = sia.polarity_scores(text)
    return popularity
    