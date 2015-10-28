import time
import praw

r = praw.Reddit('PRAW based twitter bot by '
	           'u/diaop ')

r.login()
already_done = []

prawWords = []

while True:
	subreddit = r.get_subreddit('india')
	for submission in 