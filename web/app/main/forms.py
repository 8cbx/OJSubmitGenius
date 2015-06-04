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
    country = SelectField('Country', choices=[(244,"Angola"),(93,"Afghanistan"),(355,"Albania"),(213,"Algeria"),(376,"Andorra"),(1264,"Anguilla"),(1268,"Antigua and Barbuda"),(54,"Argentina"),(374,"Armenia"),(247,"Ascension"),(61,"Australia"),(43,"Austria"),(994,"Azerbaijan"),(1242,"Bahamas"),(973,"Bahrain"),(880,"Bangladesh"),(1246,"Barbados"),(375,"Belarus"),(32,"Belgium"),(501,"Belize"),(229,"Benin"),(1441,"Bermuda Is."),(591,"Bolivia"),(267,"Botswana"),(55,"Brazil"),(673,"Brunei"),(359,"Bulgaria"),(226,"Burkina-faso"),(95,"Burma"),(257,"Burundi"),(237,"Cameroon"),(1,"Canada"),(1345,"Cayman Is."),(236,"Central African Republic"),(235,"Chad"),(56,"Chile"),(86,"China"),(57,"Colombia"),(242,"Congo"),(682,"Cook Is."),(506,"Costa Rica"),(53,"Cuba"),(357,"Cyprus"),(420,"Czech Republic"),(45,"Denmark"),(253,"Djibouti"),(1890,"Dominica Rep."),(593,"Ecuador"),(20,"Egypt"),(503,"EI Salvador"),(372,"Estonia"),(251,"Ethiopia"),(679,"Fiji"),(358,"Finland"),(33,"France"),(594,"French Guiana"),(241,"Gabon"),(220,"Gambia"),(995,"Georgia"),(49,"Germany"),(233,"Ghana"),(350,"Gibraltar"),(30,"Greece"),(1809,"Grenada"),(1671,"Guam"),(502,"Guatemala"),(224,"Guinea"),(592,"Guyana"),(509,"Haiti"),(504,"Honduras"),(852,"Hongkong"),(36,"Hungary"),(354,"Iceland"),(91,"India"),(62,"Indonesia"),(98,"Iran"),(964,"Iraq"),(353,"Ireland"),(972,"Israel"),(39,"Italy"),(225,"Ivory Coast"),(1876,"Jamaica"),(81,"Japan"),(962,"Jordan"),(855,"Kampuchea (Cambodia )"),(327,"Kazakstan"),(254,"Kenya"),(82,"Korea"),(965,"Kuwait"),(331,"Kyrgyzstan"),(856,"Laos"),(371,"Latvia"),(961,"Lebanon"),(266,"Lesotho"),(231,"Liberia"),(218,"Libya"),(423,"Liechtenstein"),(370,"Lithuania"),(352,"Luxembourg"),(853,"Macao"),(261,"Madagascar"),(265,"Malawi"),(60,"Malaysia"),(960,"Maldives"),(223,"Mali"),(356,"Malta"),(1670,"Mariana Is"),(596,"Martinique"),(230,"Mauritius"),(52,"Mexico"),(373,"Moldova, Republic of"),(377,"Monaco"),(976,"Mongolia"),(1664,"Montserrat Is"),(212,"Morocco"),(258,"Mozambique"),(264,"Namibia"),(674,"Nauru"),(977,"Nepal"),(599,"Netheriands Antilles"),(31,"Netherlands"),(64,"New Zealand"),(505,"Nicaragua"),(227,"Niger"),(234,"Nigeria"),(850,"North Korea"),(47,"Norway"),(968,"Oman"),(92,"Pakistan"),(507,"Panama"),(675,"Papua New Cuinea"),(595,"Paraguay"),(51,"Peru"),(63,"Philippines"),(48,"Poland"),(689,"French Polynesia"),(351,"Portugal"),(1787,"Puerto Rico"),(974,"Qatar"),(262,"Reunion"),(40,"Romania"),(7,"Russia"),(1758,"Saint Lueia"),(1784,"Saint Vincent"),(684,"Samoa Eastern"),(685,"Samoa Western"),(378,"San Marino"),(239,"Sao Tome and Principe"),(966,"Saudi Arabia"),(221,"Senegal"),(248,"Seychelles"),(232,"Sierra Leone"),(65,"Singapore"),(421,"Slovakia"),(386,"Slovenia"),(677,"Solomon Is"),(252,"Somali"),(27,"South Africa"),(34,"Spain"),(94,"Sri Lanka"),(1758,"St.Lucia"),(1784,"St.Vincent"),(249,"Sudan"),(597,"Suriname"),(268,"Swaziland"),(46,"Sweden"),(41,"Switzerland"),(963,"Syria"),(886,"Taiwan"),(992,"Tajikstan"),(255,"Tanzania"),(66,"Thailand"),(228,"Togo"),(676,"Tonga"),(1809,"Trinidad and Tobago"),(216,"Tunisia"),(90,"Turkey"),(993,"Turkmenistan"),(256,"Uganda"),(380,"Ukraine"),(971,"United Arab Emirates"),(44,"United Kiongdom"),(1,"United States of America"),(598,"Uruguay"),(233,"Uzbekistan"),(58,"Venezuela"),(84,"Vietnam"),(967,"Yemen"),(381,"Yugoslavia"),(263,"Zimbabwe"),(243,"Zaire"),(260,"Zambia")],coerce=int)
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
    country = SelectField('Country', choices=[(244,"Angola"),(93,"Afghanistan"),(355,"Albania"),(213,"Algeria"),(376,"Andorra"),(1264,"Anguilla"),(1268,"Antigua and Barbuda"),(54,"Argentina"),(374,"Armenia"),(247,"Ascension"),(61,"Australia"),(43,"Austria"),(994,"Azerbaijan"),(1242,"Bahamas"),(973,"Bahrain"),(880,"Bangladesh"),(1246,"Barbados"),(375,"Belarus"),(32,"Belgium"),(501,"Belize"),(229,"Benin"),(1441,"Bermuda Is."),(591,"Bolivia"),(267,"Botswana"),(55,"Brazil"),(673,"Brunei"),(359,"Bulgaria"),(226,"Burkina-faso"),(95,"Burma"),(257,"Burundi"),(237,"Cameroon"),(1,"Canada"),(1345,"Cayman Is."),(236,"Central African Republic"),(235,"Chad"),(56,"Chile"),(86,"China"),(57,"Colombia"),(242,"Congo"),(682,"Cook Is."),(506,"Costa Rica"),(53,"Cuba"),(357,"Cyprus"),(420,"Czech Republic"),(45,"Denmark"),(253,"Djibouti"),(1890,"Dominica Rep."),(593,"Ecuador"),(20,"Egypt"),(503,"EI Salvador"),(372,"Estonia"),(251,"Ethiopia"),(679,"Fiji"),(358,"Finland"),(33,"France"),(594,"French Guiana"),(241,"Gabon"),(220,"Gambia"),(995,"Georgia"),(49,"Germany"),(233,"Ghana"),(350,"Gibraltar"),(30,"Greece"),(1809,"Grenada"),(1671,"Guam"),(502,"Guatemala"),(224,"Guinea"),(592,"Guyana"),(509,"Haiti"),(504,"Honduras"),(852,"Hongkong"),(36,"Hungary"),(354,"Iceland"),(91,"India"),(62,"Indonesia"),(98,"Iran"),(964,"Iraq"),(353,"Ireland"),(972,"Israel"),(39,"Italy"),(225,"Ivory Coast"),(1876,"Jamaica"),(81,"Japan"),(962,"Jordan"),(855,"Kampuchea (Cambodia )"),(327,"Kazakstan"),(254,"Kenya"),(82,"Korea"),(965,"Kuwait"),(331,"Kyrgyzstan"),(856,"Laos"),(371,"Latvia"),(961,"Lebanon"),(266,"Lesotho"),(231,"Liberia"),(218,"Libya"),(423,"Liechtenstein"),(370,"Lithuania"),(352,"Luxembourg"),(853,"Macao"),(261,"Madagascar"),(265,"Malawi"),(60,"Malaysia"),(960,"Maldives"),(223,"Mali"),(356,"Malta"),(1670,"Mariana Is"),(596,"Martinique"),(230,"Mauritius"),(52,"Mexico"),(373,"Moldova, Republic of"),(377,"Monaco"),(976,"Mongolia"),(1664,"Montserrat Is"),(212,"Morocco"),(258,"Mozambique"),(264,"Namibia"),(674,"Nauru"),(977,"Nepal"),(599,"Netheriands Antilles"),(31,"Netherlands"),(64,"New Zealand"),(505,"Nicaragua"),(227,"Niger"),(234,"Nigeria"),(850,"North Korea"),(47,"Norway"),(968,"Oman"),(92,"Pakistan"),(507,"Panama"),(675,"Papua New Cuinea"),(595,"Paraguay"),(51,"Peru"),(63,"Philippines"),(48,"Poland"),(689,"French Polynesia"),(351,"Portugal"),(1787,"Puerto Rico"),(974,"Qatar"),(262,"Reunion"),(40,"Romania"),(7,"Russia"),(1758,"Saint Lueia"),(1784,"Saint Vincent"),(684,"Samoa Eastern"),(685,"Samoa Western"),(378,"San Marino"),(239,"Sao Tome and Principe"),(966,"Saudi Arabia"),(221,"Senegal"),(248,"Seychelles"),(232,"Sierra Leone"),(65,"Singapore"),(421,"Slovakia"),(386,"Slovenia"),(677,"Solomon Is"),(252,"Somali"),(27,"South Africa"),(34,"Spain"),(94,"Sri Lanka"),(1758,"St.Lucia"),(1784,"St.Vincent"),(249,"Sudan"),(597,"Suriname"),(268,"Swaziland"),(46,"Sweden"),(41,"Switzerland"),(963,"Syria"),(886,"Taiwan"),(992,"Tajikstan"),(255,"Tanzania"),(66,"Thailand"),(228,"Togo"),(676,"Tonga"),(1809,"Trinidad and Tobago"),(216,"Tunisia"),(90,"Turkey"),(993,"Turkmenistan"),(256,"Uganda"),(380,"Ukraine"),(971,"United Arab Emirates"),(44,"United Kiongdom"),(1,"United States of America"),(598,"Uruguay"),(233,"Uzbekistan"),(58,"Venezuela"),(84,"Vietnam"),(967,"Yemen"),(381,"Yugoslavia"),(263,"Zimbabwe"),(243,"Zaire"),(260,"Zambia")],coerce=int)
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
