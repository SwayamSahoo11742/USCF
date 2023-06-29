import datetime
import pytz
from datetime import timedelta
from textblob import TextBlob

books = {
    "book1": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": datetime.datetime.now(pytz.timezone('US/Eastern')).replace(microsecond=0),
        "genres": ["Fiction", "Classic"],
        "ratings": {
            "goodreads": 4.2,
            "amazon": 4.5,
            "bookdepository": 4.3
        },
        "reviews": [
            {
                "username": "reader1",
                "rating": 4,
                "comment": "A classic tale of love and tragedy."
            },
            {
                "username": "reader2",
                "rating": 5,
                "comment": "Beautifully written and captivating."
            }
        ]
    },
    "book2": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": datetime.datetime(2023, 6, 29, 1, 59, 45, tzinfo=datetime.timezone.utc),
        "genres": ["Fiction", "Historical"],
        "ratings": {
            "goodreads": 4.4,
            "amazon": 4.6,
            "bookdepository": 4.5
        },
        "reviews": [
            {
                "username": "reader3",
                "rating": 5,
                "comment": "A powerful and thought-provoking story."
            },
            {
                "username": "reader4",
                "rating": 4.5,
                "comment": "An important book that tackles social issues."
            }
        ]
    },
    "book3": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": datetime.datetime(2023, 6, 29, 1, 10, 45, tzinfo=datetime.timezone.utc),
        "genres": ["Fiction", "Romance"],
        "ratings": {
            "goodreads": 4.3,
            "amazon": 4.6,
            "bookdepository": 4.4
        },
        "reviews": [
            {
                "username": "reader5",
                "rating": 4.5,
                "comment": "A delightful romantic novel with memorable characters."
            },
            {
                "username": "reader6",
                "rating": 5,
                "comment": "A timeless classic that explores societal norms."
            }
        ]
    },
    "book4": {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": datetime.datetime(2023, 6, 28, 22, 10, 45, tzinfo=datetime.timezone.utc),
        "genres": ["Fiction", "Dystopian"],
        "ratings": {
            "goodreads": 4.2,
            "amazon": 4.4,
            "bookdepository": 4.3
        },
        "reviews": [
            {
                "username": "reader7",
                "rating": 4,
                "comment": "A chilling portrayal of a dystopian society."
            },
            {
                "username": "reader8",
                "rating": 4.5,
                "comment": "Thought-provoking and relevant even today."
            }
        ]
    }
}

est = datetime.timezone(datetime.timedelta(hours=0))  # Define the desired timezone (in this case, UTC)

def recently(books, day, shour):
    recent = {}
    # most recent hashtag mentions and removes any hashtags past 5 days 
    today = datetime.datetime.now().replace(microsecond=0, tzinfo=est) # current date 
    if shour != 0:
        start_time = today.replace(hour=shour,microsecond=0, tzinfo=est) 
        end_time = today.replace(hour=shour,microsecond=0, tzinfo=est) - datetime.timedelta(hours=1)
        activate = True
    else: 
        cutoff = today - timedelta(days=day, hours=shour)
        activate = False 
    for key, value in books.items():
        if activate:
            if end_time <= convert_utc_into_est(value["publication_year"]) < start_time:
                recent[key] = value
        else: 
            if convert_utc_into_est(value["publication_year"]) > cutoff:
                recent[key] = value
    return recent
def convert_utc_into_est(recent_item):
    return recent_item.astimezone(est)

print(datetime.datetime.now().replace(microsecond=0, tzinfo=est)-convert_utc_into_est(datetime.datetime(2023, 6, 28, 23, 20, 45, tzinfo=datetime.timezone.utc)))
print(recently(books,0,1))
print(datetime.datetime.now().replace(microsecond=0, tzinfo=est))
today = datetime.datetime.now().replace(microsecond=0, tzinfo=est) # current date 
start_time = today.replace(hour=1,microsecond=0, tzinfo=est) 
end_time = today.replace(hour=1,microsecond=0, tzinfo=est) - datetime.timedelta(hours=1)
print(start_time)
print( end_time
)

print(float(1.2)/(len(books) ))
print()