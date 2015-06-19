from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(Form):
    name = StringField('Nickname', validators=[Length(0, 64)])
    country = SelectField('Country', choices=[("Andorra","Andorra"),("United Arab Emirates","United Arab Emirates"),("Afghanistan","Afghanistan"),("Antigua and Barbuda","Antigua and Barbuda"),("Anguilla","Anguilla"),("Albania","Albania"),("Armenia","Armenia"),("Angola","Angola"),("Argentina","Argentina"),("Austria","Austria"),("Australia","Australia"),("Azerbaijan","Azerbaijan"),("Barbados","Barbados"),("Bangladesh","Bangladesh"),("Belgium","Belgium"),("Burkina-faso","Burkina-faso"),("Bulgaria","Bulgaria"),("Bahrain","Bahrain"),("Burundi","Burundi"),("Benin","Benin"),("Palestine","Palestine"),("Bermuda Is.","Bermuda Is."),("Brunei","Brunei"),("Bolivia","Bolivia"),("Brazil","Brazil"),("Bahamas","Bahamas"),("Botswana","Botswana"),("Belarus","Belarus"),("Belize","Belize"),("Canada","Canada"),("Central African Republic","Central African Republic"),("Congo","Congo"),("Switzerland","Switzerland"),("Cook Is.","Cook Is."),("Chile","Chile"),("Cameroon","Cameroon"),("China","China"),("Colombia","Colombia"),("Costa Rica","Costa Rica"),("Czech","Czech"),("Cuba","Cuba"),("Cyprus","Cyprus"),("Czech Republic","Czech Republic"),("Germany","Germany"),("Djibouti","Djibouti"),("Denmark","Denmark"),("Dominica Rep.","Dominica Rep."),("Algeria","Algeria"),("Ecuador","Ecuador"),("Estonia","Estonia"),("Egypt","Egypt"),("Spain","Spain"),("Ethiopia","Ethiopia"),("Finland","Finland"),("Fiji","Fiji"),("France","France"),("Gabon","Gabon"),("United Kiongdom","United Kiongdom"),("Grenada","Grenada"),("Georgia","Georgia"),("French Guiana","French Guiana"),("Ghana","Ghana"),("Gibraltar","Gibraltar"),("Gambia","Gambia"),("Guinea","Guinea"),("Greece","Greece"),("Guatemala","Guatemala"),("Guam","Guam"),("Guyana","Guyana"),("Hongkong","Hongkong"),("Honduras","Honduras"),("Haiti","Haiti"),("Hungary","Hungary"),("Indonesia","Indonesia"),("Ireland","Ireland"),("Israel","Israel"),("India","India"),("Iraq","Iraq"),("Iran","Iran"),("Iceland","Iceland"),("Italy","Italy"),("Jamaica","Jamaica"),("Jordan","Jordan"),("Japan","Japan"),("Kenya","Kenya"),("Kyrgyzstan","Kyrgyzstan"),("Kampuchea (Cambodia)","Kampuchea (Cambodia)"),("North Korea","North Korea"),("Korea","Korea"),("Republic of Ivory Coast","Republic of Ivory Coast"),("Kuwait","Kuwait"),("Kazakstan","Kazakstan"),("Laos","Laos"),("Lebanon","Lebanon"),("St.Lucia","St.Lucia"),("Liechtenstein","Liechtenstein"),("Sri Lanka","Sri Lanka"),("Liberia","Liberia"),("Lesotho","Lesotho"),("Lithuania","Lithuania"),("Luxembourg","Luxembourg"),("Latvia","Latvia"),("Libya","Libya"),("Morocco","Morocco"),("Monaco","Monaco"),("The Republic of Moldova","The Republic of Moldova"),("Madagascar","Madagascar"),("Mali","Mali"),("Burma","Burma"),("Mongolia","Mongolia"),("Macao","Macao"),("Montserrat Is","Montserrat Is"),("Malta","Malta"),("Mauritius","Mauritius"),("Maldives","Maldives"),("Malawi","Malawi"),("Mexico","Mexico"),("Malaysia","Malaysia"),("Mozambique","Mozambique"),("Namibia","Namibia"),("Niger","Niger"),("Nigeria","Nigeria"),("Nicaragua","Nicaragua"),("Netherlands","Netherlands"),("Norway","Norway"),("Nepal","Nepal"),("Nauru","Nauru"),("New Zealand","New Zealand"),("Oman","Oman"),("Panama","Panama"),("Peru","Peru"),("French Polynesia","French Polynesia"),("Papua New Cuinea","Papua New Cuinea"),("Philippines","Philippines"),("Pakistan","Pakistan"),("Poland","Poland"),("Puerto Rico","Puerto Rico"),("Portugal","Portugal"),("Paraguay","Paraguay"),("Qatar","Qatar"),("Romania","Romania"),("Russia","Russia"),("Saudi Arabia","Saudi Arabia"),("Solomon Is","Solomon Is"),("Seychelles","Seychelles"),("Sudan","Sudan"),("Sweden","Sweden"),("Singapore","Singapore"),("Slovenia","Slovenia"),("Slovakia","Slovakia"),("Sierra Leone","Sierra Leone"),("San Marino","San Marino"),("Senegal","Senegal"),("Somali","Somali"),("Suriname","Suriname"),("Sao Tome and Principe","Sao Tome and Principe"),("EI Salvador","EI Salvador"),("Syria","Syria"),("Swaziland","Swaziland"),("Chad","Chad"),("Togo","Togo"),("Thailand","Thailand"),("Tajikstan","Tajikstan"),("Turkmenistan","Turkmenistan"),("Tunisia","Tunisia"),("Tonga","Tonga"),("Turkey","Turkey"),("Trinidad and Tobago","Trinidad and Tobago"),("Taiwan","Taiwan"),("Tanzania","Tanzania"),("Ukraine","Ukraine"),("Uganda","Uganda"),("United States of America","United States of America"),("Uruguay","Uruguay"),("Uzbekistan","Uzbekistan"),("Saint Vincent","Saint Vincent"),("Venezuela","Venezuela"),("Vietnam","Vietnam"),("Yemen","Yemen"),("Yugoslavia","Yugoslavia"),("South Africa","South Africa"),("Zambia","Zambia"),("Zaire","Zaire")])
    school = StringField('School',validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Nickname', validators=[Length(0, 64)])
    country = SelectField('Country', choices=[("Andorra","Andorra"),("United Arab Emirates","United Arab Emirates"),("Afghanistan","Afghanistan"),("Antigua and Barbuda","Antigua and Barbuda"),("Anguilla","Anguilla"),("Albania","Albania"),("Armenia","Armenia"),("Angola","Angola"),("Argentina","Argentina"),("Austria","Austria"),("Australia","Australia"),("Azerbaijan","Azerbaijan"),("Barbados","Barbados"),("Bangladesh","Bangladesh"),("Belgium","Belgium"),("Burkina-faso","Burkina-faso"),("Bulgaria","Bulgaria"),("Bahrain","Bahrain"),("Burundi","Burundi"),("Benin","Benin"),("Palestine","Palestine"),("Bermuda Is.","Bermuda Is."),("Brunei","Brunei"),("Bolivia","Bolivia"),("Brazil","Brazil"),("Bahamas","Bahamas"),("Botswana","Botswana"),("Belarus","Belarus"),("Belize","Belize"),("Canada","Canada"),("Central African Republic","Central African Republic"),("Congo","Congo"),("Switzerland","Switzerland"),("Cook Is.","Cook Is."),("Chile","Chile"),("Cameroon","Cameroon"),("China","China"),("Colombia","Colombia"),("Costa Rica","Costa Rica"),("Czech","Czech"),("Cuba","Cuba"),("Cyprus","Cyprus"),("Czech Republic","Czech Republic"),("Germany","Germany"),("Djibouti","Djibouti"),("Denmark","Denmark"),("Dominica Rep.","Dominica Rep."),("Algeria","Algeria"),("Ecuador","Ecuador"),("Estonia","Estonia"),("Egypt","Egypt"),("Spain","Spain"),("Ethiopia","Ethiopia"),("Finland","Finland"),("Fiji","Fiji"),("France","France"),("Gabon","Gabon"),("United Kiongdom","United Kiongdom"),("Grenada","Grenada"),("Georgia","Georgia"),("French Guiana","French Guiana"),("Ghana","Ghana"),("Gibraltar","Gibraltar"),("Gambia","Gambia"),("Guinea","Guinea"),("Greece","Greece"),("Guatemala","Guatemala"),("Guam","Guam"),("Guyana","Guyana"),("Hongkong","Hongkong"),("Honduras","Honduras"),("Haiti","Haiti"),("Hungary","Hungary"),("Indonesia","Indonesia"),("Ireland","Ireland"),("Israel","Israel"),("India","India"),("Iraq","Iraq"),("Iran","Iran"),("Iceland","Iceland"),("Italy","Italy"),("Jamaica","Jamaica"),("Jordan","Jordan"),("Japan","Japan"),("Kenya","Kenya"),("Kyrgyzstan","Kyrgyzstan"),("Kampuchea (Cambodia)","Kampuchea (Cambodia)"),("North Korea","North Korea"),("Korea","Korea"),("Republic of Ivory Coast","Republic of Ivory Coast"),("Kuwait","Kuwait"),("Kazakstan","Kazakstan"),("Laos","Laos"),("Lebanon","Lebanon"),("St.Lucia","St.Lucia"),("Liechtenstein","Liechtenstein"),("Sri Lanka","Sri Lanka"),("Liberia","Liberia"),("Lesotho","Lesotho"),("Lithuania","Lithuania"),("Luxembourg","Luxembourg"),("Latvia","Latvia"),("Libya","Libya"),("Morocco","Morocco"),("Monaco","Monaco"),("The Republic of Moldova","The Republic of Moldova"),("Madagascar","Madagascar"),("Mali","Mali"),("Burma","Burma"),("Mongolia","Mongolia"),("Macao","Macao"),("Montserrat Is","Montserrat Is"),("Malta","Malta"),("Mauritius","Mauritius"),("Maldives","Maldives"),("Malawi","Malawi"),("Mexico","Mexico"),("Malaysia","Malaysia"),("Mozambique","Mozambique"),("Namibia","Namibia"),("Niger","Niger"),("Nigeria","Nigeria"),("Nicaragua","Nicaragua"),("Netherlands","Netherlands"),("Norway","Norway"),("Nepal","Nepal"),("Nauru","Nauru"),("New Zealand","New Zealand"),("Oman","Oman"),("Panama","Panama"),("Peru","Peru"),("French Polynesia","French Polynesia"),("Papua New Cuinea","Papua New Cuinea"),("Philippines","Philippines"),("Pakistan","Pakistan"),("Poland","Poland"),("Puerto Rico","Puerto Rico"),("Portugal","Portugal"),("Paraguay","Paraguay"),("Qatar","Qatar"),("Romania","Romania"),("Russia","Russia"),("Saudi Arabia","Saudi Arabia"),("Solomon Is","Solomon Is"),("Seychelles","Seychelles"),("Sudan","Sudan"),("Sweden","Sweden"),("Singapore","Singapore"),("Slovenia","Slovenia"),("Slovakia","Slovakia"),("Sierra Leone","Sierra Leone"),("San Marino","San Marino"),("Senegal","Senegal"),("Somali","Somali"),("Suriname","Suriname"),("Sao Tome and Principe","Sao Tome and Principe"),("EI Salvador","EI Salvador"),("Syria","Syria"),("Swaziland","Swaziland"),("Chad","Chad"),("Togo","Togo"),("Thailand","Thailand"),("Tajikstan","Tajikstan"),("Turkmenistan","Turkmenistan"),("Tunisia","Tunisia"),("Tonga","Tonga"),("Turkey","Turkey"),("Trinidad and Tobago","Trinidad and Tobago"),("Taiwan","Taiwan"),("Tanzania","Tanzania"),("Ukraine","Ukraine"),("Uganda","Uganda"),("United States of America","United States of America"),("Uruguay","Uruguay"),("Uzbekistan","Uzbekistan"),("Saint Vincent","Saint Vincent"),("Venezuela","Venezuela"),("Vietnam","Vietnam"),("Yemen","Yemen"),("Yugoslavia","Yugoslavia"),("South Africa","South Africa"),("Zambia","Zambia"),("Zaire","Zaire")])
    school = StringField('School',validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class SubmitForm(Form):
	OJ_ID=SelectField('OJ', choices=[("POJ","POJ")])
	PID=StringField('PID',validators=[Length(0, 8)])
	Language=SelectField('OJ', choices=[("0","G++"),("1","GCC"),("2","Java"),("3","Pascal"),("4","C++"),("5","C"),("6","Fortran")])
	Code=TextAreaField('Code',validators=[Required(),Length(0, 65535)])
	submit = SubmitField('Submit')
