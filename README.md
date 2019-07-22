# sentimentify
### Setting up dependencies
Run these commands to create and run your virtual environment:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
Run this command to set up dependencies:
```
$ pip install -r requirements.txt
```
Obtain your Reddit `client_id`, `client_secret` by creating an app on Reddit. Then create a JSON file containing your access token information and place it in this path:  `/assets/login_info/reddit_login.json`. The file should look like this:
```
{
    "client_id": <client_id>,
    "client_secret": <client_secret>,
    "user_agent": "sentimentify v1.0 by /u/sentimentify_bot"
}
```
### Running the program
Run this program by entering this in your command line:
```
$ export FLASK_APP=sentimentify.py
# flask run
```