from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import Permission, Role, User, Problem
from ..decorators import admin_required


@main.route('/problem', methods=['GET', 'POST'])
def indexProblem():
	page = request.args.get('page', 1, type=int)
	pagination = Problem.query.order_by(Problem.LastUpdate.desc()).paginate(
       page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
		error_out=False)
	problems = pagination.items
	return render_template('indexProblem.html',problems=problems, pagination=pagination)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/problem/<int:SID>')
def problem(SID):
    problem = Problem.query.get_or_404(SID)
    return render_template('problem.html', problems=[problem])
	 

