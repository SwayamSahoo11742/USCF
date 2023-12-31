import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import praw
import pytz
import textblob


def create_reddit_instance():
    return praw.Reddit(
        client_id="hJtFEp88TDdHYAOnJ31vuQ",
        client_secret="TFAywy_Q6-dIfEIARZOvRfg4eZl2Nw",
        user_agent="perceptify"
    )


# TODO: Save data to Supabase
def store(data):
    pass


def convert_time(utc_time):
    et = pytz.timezone('US/Eastern')
    return datetime.fromtimestamp(utc_time, tz=et).replace(minute=0, second=0, microsecond=0).isoformat()


def count_mentions(text, target):
    return text.count(target)


def compute_sentiment_score(text):
    polarity, _ = textblob.TextBlob(text).sentiment
    return (polarity + 1) * 50


def process_and_store_data(dt, text, target, mentions, sentiments):
    num_mentions = count_mentions(text, target)

    if num_mentions == 0: return

    mentions[dt] += num_mentions

    sentiment_score = compute_sentiment_score(text)

    total_sentiment_score, entry_count = sentiments[dt]
    sentiments[dt] = (total_sentiment_score + sentiment_score, entry_count + 1)


def process_comment(comment, target, mentions, sentiments):
    dt = convert_time(comment.created_utc)
    text = comment.body.lower()
    process_and_store_data(dt, text, target, mentions, sentiments)


def process_submission(submission, target, mentions, sentiments):
    # Process the title and text of the main post.
    dt = convert_time(submission.created_utc)
    text = f"{submission.title}\n\n{submission.selftext}".lower()
    process_and_store_data(dt, text, target, mentions, sentiments)
    
    # Process the comments and nested replies.
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        process_comment(comment, target, mentions, sentiments)


def analyze(reddit, target, time_filter="hour"):
    mentions = defaultdict(int)
    sentiments = defaultdict(lambda: (0, 0))

    for submission in reddit.subreddit("all").search(target, sort="new", time_filter=time_filter, limit=None):
        # print(f"https://www.reddit.com/{submission.permalink}")
        process_submission(submission, target, mentions, sentiments)

    # Compute averages.
    sentiments = {k : (total_sentiment_score / entry_count) 
                  for k, (total_sentiment_score, entry_count) in sentiments.items()}

    return mentions, sentiments


def register_company(company_name):
    reddit = create_reddit_instance()
    mentions, sentiments = analyze(reddit, company_name, time_filter="month")
    return mentions, sentiments


def process_hourly(company_name):
    reddit = create_reddit_instance()
    mentions, sentiments = analyze(reddit, company_name, time_filter="hour")
    return mentions, sentiments


# def search_time_window(target, start, time_diff):
#     for submission in reddit.subreddit("all").search(target, sort="new", limit=None):
#         if submission.created_utc - start > time_diff:
#             return
#         yield submission


# def main():
#     reddit = create_reddit_instance()
#     mentions, sentiments = analyze(reddit, "facebook", time_filter="hour")
#     print(mentions)
#     print(sentiments)