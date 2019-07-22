import math

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from app.obj.result import Result


class SentimentProcessor:
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def find_corresponding_sentiment(self, score):
        if score <= -0.4:
            return 'extremely negative'
        elif score <= -0.25:
            return 'very negative'
        elif score <= -0.1:
            return 'negative'
        elif score <= -0.04:
            return 'slightly negative'
        elif score < 0.04:
            return 'neutral'
        elif score < 0.1:
            return 'slightly positive'
        elif score < 0.25:
            return 'positive'
        elif score < 0.4:
            return 'very positive'
        else:
            return 'extremely positive'

    def get_compound_score(self, comment_list):
        total_score = 0
        for comment in comment_list:
            total_score += self.analyzer.polarity_scores(comment)['compound']
        avg_score = total_score / len(comment_list)
        return (avg_score, self.find_corresponding_sentiment(avg_score))

    def get_most_positive(self, comment_list):
        num_top_comments = math.ceil(len(comment_list) / 20) if len(comment_list) < 100 else 5
        top_comments = {}
        for comment in comment_list:
            score = self.analyzer.polarity_scores(comment)['compound']
            if len(top_comments) < num_top_comments:
                top_comments[comment] = score
            else:
                least_pos_comment = min(top_comments, key=top_comments.get)
                if score > top_comments[least_pos_comment]:
                    del top_comments[least_pos_comment]
                    top_comments[comment] = score
        return top_comments

    def get_most_negative(self, comment_list):
        num_top_comments = math.ceil(len(comment_list) / 20) if len(comment_list) < 100 else 5
        top_comments = {}
        for comment in comment_list:
            score = self.analyzer.polarity_scores(comment)['compound']
            if len(top_comments) < num_top_comments:
                top_comments[comment] = score
            else:
                least_neg_comment = max(top_comments, key=top_comments.get)
                if score < top_comments[least_neg_comment]:
                    del top_comments[least_neg_comment]
                    top_comments[comment] = score
        return top_comments

    def process_sentiment(self, comment_list):
        result = Result()
        result.compound_score = self.get_compound_score(comment_list)
        result.most_positive = self.get_most_positive(comment_list)
        result.most_negative = self.get_most_negative(comment_list)
        return result
