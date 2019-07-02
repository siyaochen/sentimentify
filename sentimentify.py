# import argparse

# from app.sentiment_app import SentimentApp


# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('reddit_submission_link', help='Link to the reddit submission you want to analyze.')
#     return parser.parse_args()

# if __name__ == '__main__':
#     args = parse_args()
#     sp = SentimentApp(args.reddit_submission_link)
#     sp.run()

from flask import Flask, render_template, request

from app.obj.input import Input


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    input_data = Input(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('main.html')

if __name__ == '__main__':
    app.run()
