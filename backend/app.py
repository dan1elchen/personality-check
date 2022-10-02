from flask import Flask

app = Flask(__name__)

from redditAnalysis import redditAnalysis
from reddit import reddit
from sentimentAnalysis import sentimentAnalysis

app.register_blueprint(redditAnalysis)
app.register_blueprint(reddit)
app.register_blueprint(sentimentAnalysis)


@app.route("/")
def hello_world():
    return "Hit!"
# python3 -m flask run      
# http://127.0.0.1:5000