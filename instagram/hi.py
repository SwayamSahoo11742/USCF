import datetime
from datetime import timedelta
import pytz
import json 
from textblob import TextBlob

est = pytz.timezone('US/Eastern')
today = datetime.datetime.now(est) # current date 
today = today.replace(microsecond=0)
print(today)
