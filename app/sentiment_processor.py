from app.retrievers.reddit_retriever import RedditRetriever
from app.retrievers.twitter_retriever import TwitterRetriever


class SentimentProcessor:

    def __init__(self):
        pass

    def get_data(self):
        reddit_retriever = RedditRetriever()
        twitter_retriever = TwitterRetriever()
        
        reddit_retriever.get_data(subreddit='nba')

    def analyze_data(self):
        pass

    def run(self):
        self.get_data()
