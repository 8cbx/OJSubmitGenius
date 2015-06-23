from flask.ext.wtf import Form
from datetime import datetime
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, DateTimeField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError

class AddContestForm(Form):
    Title = StringField('Title', validators=[Length(0, 128)])
    #Begin_Time = DateTimeField('Begine Time', format='%m/%d/%y')
    #End_Time = DateTimeField('End Time', format='%m/%d/%y')
    submil = SubmitField('Submit')
