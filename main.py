from TwitterAPI import TwitterAPI
import time
import praw
from prawoauth2 import PrawOAuth2Mini

# reddit api
APP_KEY = "dxvnhvIBtYzHLQ"
APP_SECRET = "zLzJuHj6-rmZUtME8gBVoVuR7Bw"

#twitter api
CONSUMER_KEY = "gTvaTJrqETBXt0qy6WTJ5NEbl"
CONSUMER_SECRET = " RnaEXb7XKTIjtpzjViKSj8BCNZzkxpLmRPcTEwKyZKLyN5GgUj"
ACCESS_TOKEN = "272283413-8zl6zZKsVprAdWfDjHwkIlwFFzGL2sOqpMyUTV0F"
ACCESS_TOKEN_SECRET = "jlDiBDqWtkyWprZ8c7sXgtJO5gvm8pdOwQB7Xh6MxKjvK"


reddit_client = praw.Reddit('PRAW based twitter bot by '
	           'u/weekerman ')
oauth_helper = PrawOAuth2Mini(reddit_client)

r.login()
already_done = []

prawWords = []

def main():
	while True:
	    subreddit = r.get_subreddit('india')
	    for submission in 

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('statuses/show/:%d' % 210462857140252672)
print(r.text)	