from instagrapi import Client
from instagrapi.exceptions import (
    BadPassword,
    ChallengeRequired,
    FeedbackRequired,
    LoginRequired,
    PleaseWaitFewMinutes,
    RecaptchaChallengeForm,
    ReloginAttemptExceeded,
    SelectContactPointRecoveryForm,
)
import datetime
from datetime import timedelta
from textblob import TextBlob
from supabase_py import create_client
import pytz

cl = Client()
cl.delay_range = [1, 3]
# user must login into instagram to avoid any issues 
ACCOUNT_USERNAME = ""
ACCOUNT_PASSWORD = ""
supabase_url = 'URL'
supabase_key = 'API_KEY'
supabase = create_client(supabase_url, supabase_key)
"""
Task specifications

Write a function for a specific social media. Twitter would be: def twitter_analysis(CompanyName), where CompanyName is a string

The function should be able to:

		Use appropriate APIs or web scraping to get the number of mentions + a few posts' contents mentioning CompanyName (ideally have posts from last 5 days)
		Save number of mentions on Supabase - No specific saving method ATM, we will standardize later
		Use TextBlob to get sentiment, save as a score from 0-100
		Save sentiment for each days seperately on Supabase as well

Think of this function as the first time a company signs up. 
You go through their history and give them data! Obviously free APIs have limitations so do the longest time frame you can or optimal code. Also if you reach API limit just move on you don't have to make the code wait 15 minutes to get your calls reset 
"""
est = datetime.timezone(datetime.timedelta(hours=0))

def companyRegisters(self):
    def handle_exception(self, client, e):
        if isinstance(e, BadPassword):
            client.logger.exception(e)
            client.set_proxy(self.next_proxy().href)
            if client.relogin_attempt > 0:
                self.freeze(str(e), days=7)
                raise ReloginAttemptExceeded(e)
            client.settings = self.rebuild_client_settings()
            return self.update_client_settings(client.get_settings())
        elif isinstance(e, LoginRequired):
            client.logger.exception(e)
            client.relogin()
            return self.update_client_settings(client.get_settings())
        elif isinstance(e, ChallengeRequired):
            api_path = client.last_json.get("challenge", {}).get("api_path")
            if api_path == "/challenge/":
                client.set_proxy(self.next_proxy().href)
                client.settings = self.rebuild_client_settings()
            else:
                try:
                    client.challenge_resolve(client.last_json)
                except ChallengeRequired as e:
                    self.freeze("Manual Challenge Required", days=2)
                    raise e
                except (
                    ChallengeRequired,
                    SelectContactPointRecoveryForm,
                    RecaptchaChallengeForm,
                ) as e:
                    self.freeze(str(e), days=4)
                    raise e
                self.update_client_settings(client.get_settings())
            return True
        elif isinstance(e, FeedbackRequired):
            message = client.last_json["feedback_message"]
            if "This action was blocked. Please try again later" in message:
                self.freeze(message, hours=12)
                    # client.settings = self.rebuild_client_settings()
                    # return self.update_client_settings(client.get_settings())
            elif "We restrict certain activity to protect our community" in message:
                # 6 hours is not enough
                self.freeze(message, hours=12)
            elif "Your account has been temporarily blocked" in message:
                """
                Based on previous use of this feature, your account has been temporarily blocked from taking this action. This block will expire on 2020-03-27.
                """
                self.freeze(message)
            elif isinstance(e, PleaseWaitFewMinutes):
                self.freeze(str(e), hours=1)
            raise e
    cl.handle_exception = handle_exception
    cl.load_settings("session.json")
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    cl.dump_settings("session.json")
    cl.get_timeline_feed()
    cl.set_country("US")
    return cl 
def total_mentions(s):
    hashtag = cl.hashtag_related_hashtags(s)
    total = int(len(hashtag)) 
    return total 
# posts from the last 5 days into a nested dictionary
def recent_posts(s,day):
    recent = {}
    companyRegisters(s)
    # most recent hashtag mentions and removes any hashtags past 5 days 
    recently = cl.hashtag_medias_recent(s, amount = 100)
    cutoff = today() - timedelta(days=day)
    for key, value in recently.items():
       if convert_utc_into_est(value["taken_at"]) > cutoff:
                recent[key] = value
    return recent
def convert_utc_into_est(recent_item):
    return recent_item.astimezone(est)
def today():
    return datetime.datetime.now().replace(microsecond=0, tzinfo=est)
# [0,100]
def get_polarity(text): 
    return (TextBlob(text).polarity + 1)*50 
def get_sentiment(text):
    return (TextBlob(text).sentiment + 1) * 50 

def updateForDay(s,day_filter):
    recent_5_days = recent_posts(s,5)
    days_posts = {}
    end_time = today().replace(day=day_filter,microsecond=0, tzinfo=est) 
    start_time = end_time - datetime.timedelta(days=1)
    for key, value in recent_5_days.items():
        if start_time <= convert_utc_into_est(value["taken_at"]) < end_time:
                days_posts[key] = value
    return sentiment_analysis(days_posts)

def updateForHour(s, day_filter, hour_filter): 
    recent_5_days = recent_posts(s,5)
    hour_posts = {}
    end_time = today().replace(day=day_filter, hour=hour_filter,microsecond=0, tzinfo=est) 
    start_time = end_time - datetime.timedelta(hours=1)
    for key, value in recent_5_days.items():
        if start_time <= convert_utc_into_est(value["taken_at"]) < end_time:
                hour_posts[key] = value
    total = 0 
    return sentiment_analysis(hour_posts)
    
# store data into supabase 
def instagram_analysis(s):
    recent_posts(s, 5)
    updateForHour(s, recent_posts(s, 1))

def sentiment_analysis(posts):
    total = 0
    for key, value in posts.items():
        if value["caption_text"]:
            sentiment = get_sentiment(value["caption_text"])
            total += sentiment 
    total_sentiment = total / (len(posts))
    return total_sentiment
    
# runs analysis 
def main():
    company_name = "perceptify" # example 
    companyRegisters(company_name)
    instagram_analysis(company_name)
    print("Total amount of mentions for hashtag : %d" % total_mentions(company_name))
    print()