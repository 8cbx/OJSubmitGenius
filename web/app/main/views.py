from flask import render_template, redirect, url_for, abort, flash
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import Role, User, Problem
from ..decorators import admin_required


@main.route('/problem', methods=['GET', 'POST'])
def indexProblrm():
	problems = Problem.query.order_by(Problem.LastUpdate.desc()).all()
	return render_template('indexProblem.html', problems = problems)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

