from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class NewTripForm(Form):
	destination = StringField('destination', validators=[DataRequired()])
	origin = StringField('origin', validators=[DataRequired()])
	contact = StringField('destination', validators=[DataRequired()])
	day = StringField('destination', validators=[DataRequired()])
	depart_time = StringField('destination', validators=[DataRequired()])
	arrival_time = StringField('destination', validators=[DataRequired()])
	seats_num = StringField('destination', validators=[DataRequired()])

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)