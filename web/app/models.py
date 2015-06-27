from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request
from flask.ext.login import UserMixin, AnonymousUserMixin
from . import db, login_manager
from OJ_Status import CheckOjStatus

class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Accepted_Problem(db.Model):
      __tablename__ = 'AC_problems'
      AC_problems_SID = db.Column(db.Integer, db.ForeignKey('problems.SID'),
                            primary_key=True)
      AC_user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                            primary_key=True)
      AC_time = db.Column(db.DateTime, default=datetime.utcnow)

class Contest_Problem(db.Model):
      __tablename__ = 'Contest_Problems'
      problems_SID = db.Column(db.Integer, db.ForeignKey('problems.SID'),
                            primary_key=True)
      Contest_id = db.Column(db.Integer, db.ForeignKey('contest.id'),
                            primary_key=True)
      Add_time = db.Column(db.DateTime, default=datetime.utcnow)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    country = db.Column(db.String(64),default='China')
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))
    school = db.Column(db.String(64))
    account_POJ = db.Column(db.String(64), default='NU LL')
    password_POJ = db.Column(db.String(64))
    followed = db.relationship('Follow',
                               foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'),
                               lazy='dynamic',
                               cascade='all, delete-orphan')

    followers = db.relationship('Follow',
                                foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

    AC_problems = db.relationship('Accepted_Problem',
                                foreign_keys=[Accepted_Problem.AC_user_id],
                                backref=db.backref('AC_user', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(
                self.email.encode('utf-8')).hexdigest()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        return self.followed.filter_by(
            followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        return self.followers.filter_by(
            follower_id=user.id).first() is not None

    def add_accepted_problem(self, problem):
        if not self.is_accepted(problem):
            f = Accepted_Problem(AC_problems=problem, AC_user=self)
            db.session.add(f)

    def is_accepted(self, problem):
        return self.AC_problems.filter_by(
            AC_problems_SID=problem.SID).first() is not None 

    def __repr__(self):
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Problem(db.Model):
	__tablename__ = 'problems'
	SID = db.Column(db.Integer, primary_key=True)
	OJ_ID = db.Column(db.String(64))
	PID = db.Column(db.Integer)
	Title = db.Column(db.String(128))
	Total_Submissions = db.Column(db.Integer)
	Accepted = db.Column(db.Integer)	
	LastUpdate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	AC_user = db.relationship('Accepted_Problem',
                                foreign_keys=[Accepted_Problem.AC_problems_SID],
                                backref=db.backref('AC_problems', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

	Contest = db.relationship('Contest_Problem',
                                foreign_keys=[Contest_Problem.problems_SID],
                                backref=db.backref('Problem', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')


class Problem_detail():
	SID=''
	OJ_ID=''
	PID=0
	Title=''
	Time_Limit=''
	Memory_Limit=''
	Total_Submissions=0
	Accepted=0
	Special_Judge=''
	Description=[]
	Input=[]
	Output=[]
	Sample_Input=[]
	Sample_Output=[]
	Hint=[]
	Source=''

class Code_detail(db.Model):
	__tablename__ = 'status'
	RunID=db.Column(db.Integer, primary_key=True)
	user=db.Column(db.String(64))
	OJ_ID=db.Column(db.String(64))
	PID = db.Column(db.Integer)
	SID = db.Column(db.Integer)
	RemoteID=db.Column(db.String(64))
	Result=db.Column(db.String(64))
	Memory=db.Column(db.String(64))
	Time=db.Column(db.String(64))
	Language=db.Column(db.String(64))
	Code_Length=db.Column(db.String(64))
	CEfile=db.Column(db.String(64))
	Contest_ID=db.Column(db.Integer)
	Submit_Time=db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Contest(db.Model):
	__tablename__ = 'contest'
	id=db.Column(db.Integer, primary_key=True)
	Title=db.Column(db.String(128))
	Begin_time=db.Column(db.DateTime, index=True, default=datetime.utcnow)
	End_time=db.Column(db.DateTime, index=True, default=datetime.utcnow)
	Openness=db.Column(db.Integer)
	Manager=db.Column(db.String(64))
	Contest_problems = db.relationship('Contest_Problem',
                                foreign_keys=[Contest_Problem.Contest_id],
                                backref=db.backref('Contest', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

	def add_problem(self, problem):
           if not self.is_add_problem(problem):
              f = Contest_Problem(problems_SID=problem.SID, Contest_id=self.id)
              db.session.add(f)

	def is_add_problem(self, problem):
           return self.Contest_problems.filter_by(
               problems_SID=problem.SID).first() is not None

	def delete_problem(self, SID):
           f = self.Contest_problems.filter_by(problems_SID=SID).first()
           if f:
               db.session.delete(f)


class OJ_Status(db.Model):
	__tablename__ = 'oj_status'
	OJ_ID=db.Column(db.String(64), primary_key=True)
	OJ_Status=db.Column(db.Boolean, default=False)
	Last_Update=db.Column(db.DateTime, index=True, default=datetime.utcnow)
	def ping(self):
		self.Last_Update = datetime.utcnow()
		self.OJ_Status=CheckOjStatus(self.OJ_ID)
		print self.OJ_Status
		db.session.add(self)
