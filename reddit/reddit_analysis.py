import datetime
import json
import os
from pathlib import Path

import praw
import textblob

# Save number of mentions on SupaBase
# Save sentiment for each day for the past 5 days on SupaBase
"""
data = {
    "date": now.strftime("%Y-%m-%d"),
    "keyword": keyword,
    "mentions": count
}
"""

def create_reddit_instance():
    return praw.Reddit(
        client_id="hJtFEp88TDdHYAOnJ31vuQ",
        client_secret="TFAywy_Q6-dIfEIARZOvRfg4eZl2Nw",
        user_agent="perceptify"
    )


def store_data(data):
    pass

def analyze(reddit, target, subreddit="all", time_filter="hour"):

    num_mentions = 0
    sentiments = []
    def process_comment(comment):
        nonlocal num_mentions

        text = comment.body
        num_mentions += text.count(target)

        if num_mentions == 0: return

        polarity, _ = textblob.TextBlob(text).sentiment
        polarity *= 100

        sentiments.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "keyword": keyword,
            "sentiment": polarity
        })

    for submission in reddit.subreddit(subreddit).search(target, time_filter=time_filter, limit=None):
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            process_comment(comments)

    return num_mentions, sentiments
