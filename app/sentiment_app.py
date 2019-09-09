from app.obj.result import Result
from app.processors.sentiment_processor import SentimentProcessor
from app.retrievers.reddit_retriever import RedditRetriever


class SentimentApp:

    def __init__(self, reddit_submission_link, use_custom_classifier):
        self.reddit_submission_link = reddit_submission_link
        self.use_custom_classifier = use_custom_classifier

    def get_data(self):
        reddit_retriever = RedditRetriever()
        comment_list = reddit_retriever.get_data(self.reddit_submission_link)
        return comment_list

    def analyze_data(self, comment_list):
        sentiment_processor = SentimentProcessor(custom=self.use_custom_classifier)
        result = sentiment_processor.process_sentiment(comment_list)
        return result

    def run(self):
        comments = self.get_data()
        result = self.analyze_data(comments)
        return result
