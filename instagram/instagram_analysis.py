from instagrapi import Client

cl = Client()
cl.delay_range = [1, 3]
cl.load_settings("session.json")
cl.login("testuser_888", "candycandy408")
#cl.dump_settings("session.json")
cl.get_timeline_feed()
#print(cl.account_info().dict())


def searchHashtag(s):
    hashtag = cl.hashtag_info(s)
    print('media count: '+ str(hashtag.dict()['media_count']))
    top = cl.hashtag_medias_top(s, amount=2)
    print(top[0].dict())
    recent = cl.hashtag_medias_recent(s, amount=2)
    print(recent[0].dict())

searchHashtag('blackpink')