from instagrapi import Client
from datetime import datetime, timedelta
from textblob import TextBlob
from supabase_py import create_client

cl = Client()
cl.delay_range = [1, 3]
cl.load_settings("session.json")
# user must login into instagram to avoid any issues 
cl.login("USERNAME", "PASSWORD")
cl.get_timeline_feed()
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

# checks the number of mentions on instagram
def instagram_analysis(s):
    # number of hashtags about company 
        hashtag = cl.hashtag_related_hashtags(s)
        total = int(hashtag.dict()['media_count'])
        print('media count: '+ str(hashtag.dict()['media_count']))
    # most recent hashtag mentions and removes any hashtags past 5 days 
        recent = cl.hashtag_medias_recent(s, amount = 100)
        today = datetime.now()
        for key, value in recent.items():
            if 'taken_at' in value:
                if recent - value['taken_at'] > timedelta(days=5):
                    del recent[key]
        # saves values into supabase 
        save_into_supabase(total)

        def save_into_supabase(total):
            dv
            
# runs analysis 
company_name = "google" # example 
instagram_analysis(company_name)