import json
import praw
import re


class RedditRetriever:

    LOGIN_CREDENTIALS_FILE_PATH = 'assets/login_info/reddit_login.json'

    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]#]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

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

    def tokenize_comments(self, comments):
        all_comments = [RedditRetriever.REPLACE_NO_SPACE.sub('', comment.body.lower()) for comment in comments]
        all_comments = [RedditRetriever.REPLACE_WITH_SPACE.sub(' ', comment) for comment in all_comments]
        # Strip all emojis from comments
        all_comments = [comment.encode('ascii', 'ignore').decode('ascii') for comment in all_comments]
        return all_comments

    def get_data(self, submission_link):
        submission = self.get_submission(submission_link)
        submission.comments.replace_more(limit=None)
        processed_comments = self.tokenize_comments(submission.comments.list())
        return processed_comments
