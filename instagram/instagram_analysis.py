from instagrapi import Client
import datetime

from datetime import timedelta
from textblob import TextBlob
from supabase_py import create_client
import pytz

cl = Client()
cl.delay_range = [1, 3]
# user must login into instagram to avoid any issues 

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
est = pytz.timezone('US/Eastern')
recent = []
# checks the number of mentions on instagram
def companyRegisters(s):
   cl.load_settings("session.json")
   cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, VERIFICATION_CODE)
   cl.dump_settings("session.json")
   cl.get_timeline_feed()
   cl.set_country("US")
   return 
def instagram_analysis(s):
    # number of hashtags about company 
    global recent 
    hashtag = cl.hashtag_related_hashtags(s)
    total = int(len(hashtag)) 
    print("Total amount of mentions for hashtag : %d" % total) # hashtag.dict()['media_count']))
    # most recent hashtag mentions and removes any hashtags past 5 days 
    recently = cl.hashtag_medias_recent(s, amount = 100)
    today = datetime.datetime.now(est) # current date 
    today = today.replace(microsecond=0)
    for key, value in recently.items():
        if 'taken_at' in value:
            if today - convert_utc_into_est(recently_get('taken_at')) > timedelta(days=5):
                del recently[key]
    
    recent.append(recently)
    return 
def convert_utc_into_est(recent_item):
    modified_date = recent_item.astimezone(est)
    return modified_date

def updateForHour(s, time): 

# store data into supabase 
def store(data):
    pass 
def sentiment_analysis():
    updateForHour
# runs analysis 
company_name = "perceptify" # example 
companyRegisters(company_name)
instagram_analysis(company_name)
sentiment_anaylsis()