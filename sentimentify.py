import argparse

from app.sentiment_app import SentimentApp


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('reddit_submission_link', help='Link to the reddit submission you want to analyze.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    sp = SentimentApp(args.reddit_submission_link)
    sp.run()
