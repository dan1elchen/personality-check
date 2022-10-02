import praw
import os 
from dotenv import load_dotenv
from flask import Blueprint
from flask import request

reddit = Blueprint("reddit", __name__)

load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

reddit_read_only = praw.Reddit(client_id=client_id, 
                                client_secret=client_secret,
                                user_agent=user_agent)

@reddit.route("/get-reddit-info/<id>/<title>")
def getRedditInfo(id, title):
    try:
        url = "https://www.reddit.com/r/BostonU/comments/" + id + "/" + title
        print(url)
        submission = reddit_read_only.submission(url={url})
        redditInfo = {"title":submission.title, "selftext":submission.selftext, "comments":[]}

        for comment in submission.comments:
            redditInfo["comments"].append(comment.body)

        print(redditInfo)
        return {"success": True, "redditInfo": redditInfo}
    except:
        print('hi')
        return {"success": False}

@reddit.route("/reddit/<id>")
def test(id):
    return id