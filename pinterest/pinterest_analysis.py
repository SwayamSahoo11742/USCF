from selenium import webdriver
from bs4 import BeautifulSoup
import time
import selenium
import requests
from selenium.webdriver.common.by import By
from textblob import TextBlob
from supabase_py import create_client, Client
from datetime import datetime
from pytz import timezone
from collections import defaultdict
TZ = timezone('EST')


supabase_url = 'URL'
supabase_key = 'API_KEY'
supabase: Client = create_client(supabase_url, supabase_key)

def pinterest_analysis(company_name):
    mentions = defaultdict(-1)
    sentiment = defaultdict(-1)
    pins = getPins(company_name)
    sentiment = getSentiment(pins)
    storeData(len(pins), sentiment, mentions, sentiment)

def getPins(query):
    url = "https://in.pinterest.com/search/pins/?q=" + query
    query = query.lower()

    options = webdriver.ChromeOptions() 
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    SLEEPTIME = 0.5
    all_pins = set()
    while True:
        # Scroll to mew height
        current_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load rest of the page
        time.sleep(SLEEPTIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Get all pins
        pins = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
        for pin in pins:
            all_pins.add(pin.text.strip())

        # Check if we have reached the bottom of the page
        if new_height == current_height:
            break
    
    

    return all_pins

def getSentiment(pins):
    total = []
    for pin in pins:
        analysis = TextBlob(pin)
        total.append(analysis.sentiment.polarity)

    sentiment = sum(total) / len(total)

    # Scaling out of 100

    sentiment = (sentiment+1)*50

    return int(sentiment)


def storeData(pins_count, sentiment, mention_dict, sentiment_dict):
    timestamp = datetime.now(TZ).strftime('%Y-%m-%d %H')
    mention_dict[timestamp] = pins_count
    sentiment_dict[timestamp] = sentiment
     

