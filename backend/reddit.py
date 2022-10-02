import praw
import os 
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

reddit_read_only = praw.Reddit(client_id=client_id, 
                                client_secret=client_secret,
                                user_agent=user_agent)

url="https://www.reddit.com/r/BostonU/comments/xsvq2a/finding_your_people/"
submission = reddit_read_only.submission(url=url)


print("post text:", submission.title, "\n")
print("self text:", submission.selftext, "\n")

for comment in submission.comments:
    print("comments:", comment.body, "\n")
print("end")
