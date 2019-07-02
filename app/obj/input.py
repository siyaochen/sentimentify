from wtforms import Form, StringField, validators

class Input(Form):
    url_link = StringField('URL', validators.URL)