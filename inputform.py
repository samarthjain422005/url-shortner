from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import URL, DataRequired, EqualTo, ValidationError, Length, Regexp, EqualTo, Optional, InputRequired, NumberRange, AnyOf, Optional


class InputForm(FlaskForm):
    url_input= StringField("URL", validators=[URL(message="Please enter a valid URL."), DataRequired()])
    submit= SubmitField("Shorten")

class SearchForm(FlaskForm):
    search_input= StringField("Search", validators=[DataRequired()])
    submit= SubmitField("Search")