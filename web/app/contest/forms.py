from flask.ext.wtf import Form
from datetime import datetime
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import Required, Length, Email, Regexp, NumberRange
from wtforms import ValidationError

class AddContestForm(Form):
    Title = StringField('Title', validators=[Length(0, 128)])
    Problem_OJ_ID = SelectField('OJ Name', choices=[("POJ","POJ")])
    Problem_PID = IntegerField('PID', validators=[NumberRange(min=0, max=100000)])
    Begin_Time = DateTimeField('Begine Time', format='Y-m-d H:i:s')
    End_Time = DateTimeField('End Time', format='Y-m-d H:i:s')
    submil = SubmitField('Submit')
