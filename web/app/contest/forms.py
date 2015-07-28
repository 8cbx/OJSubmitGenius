from flask.ext.wtf import Form
from datetime import datetime
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import Required, Length, Email, Regexp, NumberRange
from wtforms import ValidationError

class AddContestForm(Form):
    Title = StringField('Title', validators=[Length(0, 128)])
    Begin_Time = DateTimeField('Begine Time', format='Y-m-d H:i:s')
    End_Time = DateTimeField('End Time', format='Y-m-d H:i:s')
    submil = SubmitField('Submit')

class AddContestProblemForm(Form):
	Problem_OJ_ID = SelectField('OJ Name', choices=[("POJ","POJ")])
	Problem_PID = IntegerField('PID', validators=[NumberRange(min=0, max=100000)])
	submil = SubmitField('Add!')

class StatusFilter(Form):
	PID=StringField('PID',validators=[Length(0, 8)])
	OJ_ID=SelectField('OJ', choices=[('','All'),("POJ","POJ")])
	user=StringField('User Name',validators=[Length(0, 64)])
	Result=SelectField('Result', choices=[('','All'),("Accepted","Accepted"),('Presentation Error','Presentation Error'),('Time Limit Exceeded','Time Limit Exceeded'),('Memory Limit Exceeded','Memory Limit Exceeded'),('Wrong Answer','Wrong Answer'),('Runtime Error','Runtime Error'),('Output Limit Exceeded','Output Limit Exceeded'),('Compile Error','Compile Error')])
	submit = SubmitField('Filter!')
class SubmitForm(Form):
	OJ_ID=SelectField('OJ', validators=[Required()],choices=[('','All'),("POJ","POJ")])
	PID=StringField('PID',validators=[Required(),Length(0, 8)])
	Language=SelectField('Language', validators=[Required()],choices=[("0","G++"),("1","GCC"),("2","Java"),("3","Pascal"),("4","C++"),("5","C"),("6","Fortran")])
	Code=TextAreaField('Code',validators=[Required()])
	submit = SubmitField('Submit')
	def validate_Code(self, field):
		if len(field.data) < 10 or len(field.data) > 65535 :
			raise ValidationError('Code length must be between 10 and 65535 characters long!')
class ProblemFilter(Form):
	OJ_ID=SelectField('OJ', choices=[('','All'),("POJ","POJ")])
	PID=StringField('PID',validators=[Length(0, 8)])
	submit = SubmitField('Filter!')
	
class StatusFilter(Form):
	PID=StringField('PID',validators=[Length(0, 8)])
	OJ_ID=SelectField('OJ', choices=[('','All'),("POJ","POJ")])
	user=StringField('User Name',validators=[Length(0, 64)])
	Result=SelectField('Result', choices=[('','All'),("Accepted","Accepted"),('Presentation Error','Presentation Error'),('Time Limit Exceeded','Time Limit Exceeded'),('Memory Limit Exceeded','Memory Limit Exceeded'),('Wrong Answer','Wrong Answer'),('Runtime Error','Runtime Error'),('Output Limit Exceeded','Output Limit Exceeded'),('Compile Error','Compile Error')])
	submit = SubmitField('Filter!')
