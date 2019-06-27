# sentimentify
### Dependencies
Run these commands to install dependencies:
```
pip install praw
pip install tweepy
pip install vaderSentiment
```
### Running this program
First obtain a `client_id`, `client_secret` by creating an app on Reddit. Then create a JSON file containing only `client_id`, `client_secret`, and a `user_agent` that you define yourself and place it in this path:
```
/assets/login_info/reddit_login.json
```
Run this program by entering this in your command line:
```
python3 sentimentify.py <reddit_submission_link>
```