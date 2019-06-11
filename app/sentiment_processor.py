from app.retrievers.reddit_retriever import RedditRetriever
from app.retrievers.twitter_retriever import TwitterRetriever


class SentimentProcessor:

    def __init__(self):
        pass

    def get_data(self):
        reddit_retriever = RedditRetriever()
        twitter_retriever = TwitterRetriever()

    def analyze_data(self):
        pass

    def run(self):
        self.get_data()
