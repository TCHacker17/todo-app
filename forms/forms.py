from flask_wtf import FlaskForm
from wtforms import

class LogInForm(FlaskForm):
	email = EmailField