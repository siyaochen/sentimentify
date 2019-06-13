from app.retrievers.reddit_retriever import RedditRetriever
from app.retrievers.twitter_retriever import TwitterRetriever


class SentimentProcessor:

    def __init__(self, reddit_submission_link):
        self.reddit_submission_link = reddit_submission_link

    def get_data(self):
        reddit_retriever = RedditRetriever()
        comment_list = reddit_retriever.get_data(self.reddit_submission_link)

    def analyze_data(self):
        pass

    def run(self):
        self.get_data()
