import datetime
from datetime import timedelta
import pytz
time = datetime.datetime(2020, 10, 8, 7, 6, 0, tzinfo=datetime.timezone.utc)
time2 = datetime.datetime(2020, 10, 5, 7, 6, 0, tzinfo=datetime.timezone.utc)

est = pytz.timezone('US/Eastern')

esttime = time.astimezone(est)
esttime2 = time2.astimezone(est)
if(esttime-esttime2 > timedelta(days=5)):
    print("hi")