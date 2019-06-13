import praw
import json


class RedditRetriever:

    LOGIN_CREDENTIALS_FILE_PATH = 'assets/login_info/reddit_login.json'

    def __init__(self, data_size=100):
        self.data_size = data_size

    def get_submission(self, submission_link):
        with open(RedditRetriever.LOGIN_CREDENTIALS_FILE_PATH) as login_file:
            login_credentials = json.load(login_file)
        reddit = praw.Reddit(client_id=login_credentials['client_id'],
                             client_secret=login_credentials['client_secret'],
                             user_agent=login_credentials['user_agent'])
        submission = reddit.submission(url=submission_link)
        return submission
    
    def get_data(self, submission_link):
        submission = self.get_submission(submission_link)
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            print(top_level_comment.body)
