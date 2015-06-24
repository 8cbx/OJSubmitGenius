from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import current_user
from .forms import AddContestForm
from ..models import Contest, Problem
from .. import db
from . import contest

@contest.route('/add_contest', methods=['GET', 'POST'])
def add_contest():
    form = AddContestForm()
    if form.validate_on_submit():
        contest = Contest(Title=form.Title.data, 
                    Begin_time=form.Begin_Time.data,
                    End_time=form.End_Time.data,
                    Manager=current_user.username)
        db.session.add(contest)
        problems=Problem.query.filter_by(OJ_ID=form.Problem_OJ_ID.data, PID=form.Problem_PID.data).first()
        contest.add_problem(problems)
        flash('The contest has been added.')
        return redirect(url_for('contest.indexContest'))
    return render_template('add_contest.html', form=form)

@contest.route('/contests')
def indexContest():
    page = request.args.get('page', 1, type=int)
    pagination = Contest.query.order_by(Contest.id.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    contest = pagination.items
    return render_template('indexContest.html', contest=contest,
                           pagination=pagination)

