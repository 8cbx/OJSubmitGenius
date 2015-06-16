from flask import render_template, redirect, url_for, abort, flash
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import Role, User, Problem
from ..decorators import admin_required


@main.route('/', methods=['GET', 'POST'])
def index():
	problems = Problem.query.order_by(Problem.LastUpdate.desc()).all()
	return render_template('index.html', problems = problems)

