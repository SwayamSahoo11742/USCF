from analysis.save.save import save
from analysis.pinterest.pinterest_analysis import pinterest_analysis
from analysis.reddit.reddit_analysis import analyze, create_reddit_instance
from analysis.instagram.instagram_analysis import instagram_analysis, total_mentions, companyRegisters
# from twitter.twitter_analysis import
import json
from datetime import datetime
from pytz import timezone

TZ = timezone('EST')
with open("analysis\media_id.json", "r") as file:
    IDS = json.load(file)

def run_analysis(comp_id, query):
    timestamp = datetime.now(TZ).strftime('%Y-%m-%d %H')
    
    # Pinterest
    res = pinterest_analysis(query)
    print(res)
    pinterest_data = {
        "company_id":comp_id,
        "media_id":IDS["pinterest"],
        "mention_count": res["count"],
        "relevance_score": res["sentiment"],
        "timestamp": timestamp
    }
    
    # Reddit
    reddit = create_reddit_instance()
    mentions, sentiments = analyze(reddit, query, time_filter="hour")
    reddit_data = {
        "company_id":comp_id,
        "media_id":IDS["reddit"],
        "mention_count": mentions[list(mentions.keys())[-1]],
        "relevance_score": int(sentiments[list(sentiments.keys())[-1]]), 
        "timestamp": timestamp
    }    
    
    # Instagram
    companyRegisters(query)
    insta_mentions = total_mentions(query)
    sentiment = instagram_analysis(query)
    insta_data = {
        "company_id":comp_id,
        "media_id":IDS["reddit"],
        "mention_count": insta_mentions,
        "relevance_score": sentiment, 
        "timestamp": timestamp
    }  
    
    save("data", reddit_data)
    save("data", pinterest_data)
    save("data", insta_data)

    
