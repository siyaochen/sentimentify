import praw
import json


class RedditRetriever:

    LOGIN_CREDENTIALS_FILE_PATH = 'assets/login_info/reddit_login.json'

    def __init__(self, data_size=100):
        self.data_size = data_size

    def get_subreddit(self, subreddit_name):
        with open(RedditRetriever.LOGIN_CREDENTIALS_FILE_PATH) as login_file:
            login_credentials = json.load(login_file)
        reddit = praw.Reddit(client_id=login_credentials['client_id'],
                             client_secret=login_credentials['client_secret'],
                             user_agent=login_credentials['user_agent'])
        subreddit = reddit.subreddit(subreddit_name)
        return subreddit
    
    def get_data(self, subreddit):
        sub = self.get_subreddit(subreddit)
        try:
            for post in sub.hot(limit=10):
                print(post.title)
        except Exception as e:
            print('Error, unable to access /r/{}.'.format(subreddit))
