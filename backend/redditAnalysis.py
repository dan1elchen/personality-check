from reddit import *
from sentimentanalysis import *

def parseRedditPost(redditInfo):
    title_score = popularityScore(redditInfo["title"])
    selftext_score = popularityScore(redditInfo["selftext"])
    comment_scores = [popularityScore(comment) for comment in redditInfo["comments"]]
    comment_neg_score = sum([score_dict["neg"] for score_dict in comment_scores])/len(comment_scores)
    comment_neu_score = sum([score_dict["neu"] for score_dict in comment_scores])/len(comment_scores)
    comment_pos_score = sum([score_dict["pos"] for score_dict in comment_scores])/len(comment_scores)

    total_neg_score = title_score["neg"] * .25 + selftext_score["neg"] * .25 + comment_neg_score * .5
    total_neu_score = title_score["neu"] * .25 + selftext_score["neu"] * .25 + comment_neu_score * .5
    total_pos_score = title_score["pos"] * .25 + selftext_score["pos"] * .25 + comment_pos_score * .5

    return [total_neg_score, total_neu_score, total_pos_score]