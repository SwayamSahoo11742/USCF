import praw
import requests
import datetime
import json
import os

reddit = praw.Reddit(client_id='hJtFEp88TDdHYAOnJ31vuQ', client_secret='TFAywy_Q6-dIfEIARZOvRfg4eZl2Nw', user_agent='perceptify')

#input
keyword = input("Enter keyword: ")
focusSubreddit = input("Enter subreddit name: ")

#set initial count
count = 0

#scrape keyword mentions
for submission in reddit.subreddit('all').search(keyword, limit=5):
    url = 'https://www.reddit.com'+submission.permalink
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if keyword in response.text:
        count += 1

for submission in reddit.subreddit('entrepreneur').search(keyword, limit=5):
    url = 'https://www.reddit.com'+submission.permalink
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if keyword in response.text:
        count += 1

for submission in reddit.subreddit('startups').search(keyword, limit=5):
    url = 'https://www.reddit.com'+submission.permalink
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if keyword in response.text:
        count += 1

subreddit = reddit.subreddit(focusSubreddit)

#comments from top posts (current limit 5)
for post in subreddit.top(limit=5):
    post.comments.replace_more(limit=None)
    comments = post.comments.list()[:5] #top 5 comments
    for comment in comments:
        if keyword in comment.body.lower():
            count += 1

#current date
now = datetime.datetime.now()

#json
data = {
    "date": now.strftime("%Y-%m-%d"),
    "keyword": keyword,
    "mentions": count
}
json_data = json.dumps(data)
with open("data.json", "w") as f:
    f.write(json_data)