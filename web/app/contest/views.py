from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import current_user
from .forms import AddContestForm, AddContestProblemForm
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
        flash('The contest has been added.')
        return redirect(url_for('contest.indexContest'))
    return render_template('add_contest.html', form=form)

@contest.route('/modify_contest', methods=['GET', 'POST'])
def modify_contest():
	page = request.args.get('page', 1, type=int)
	contest_id = request.args.get('id', -1, type=int)
	print contest_id
	contest = Contest.query.filter_by(id=contest_id).first()
	if contest is None:
		flash('Invalid contest.')
		return redirect(url_for('.indexContest'))
	contest_problem=contest.Contest_problems.filter_by(Contest_id=contest_id)
	problem=[]
	for values in contest_problem:
		in_problem=Problem.query.filter_by(SID=values.problems_SID).first()
		problem.append(in_problem)
	print problem
	delete_PID = request.args.get('delete', -1, type=int)
	if delete_PID!=-1:
		print "Delete "+str(delete_PID)
	form = AddContestProblemForm()
	if form.validate_on_submit():
		problems=Problem.query.filter_by(OJ_ID=form.Problem_OJ_ID.data, PID=form.Problem_PID.data).first()
		if problems is None:
			flash('Problem does not exist!')
			return redirect(url_for('contest.modify_contest',id=contest_id))
		contest.add_problem(problems)
		flash('The problem has been added.')
		return redirect(url_for('contest.modify_contest',id=contest_id))
	return render_template('modify_contest.html', form=form,problem=problem,contest=contest)
	

@contest.route('/contests')
def indexContest():
    page = request.args.get('page', 1, type=int)
    pagination = Contest.query.order_by(Contest.id.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    contest = pagination.items
    return render_template('indexContest.html', contest=contest,
                           pagination=pagination)

@contest.route('/Contest/<int:id>')
def contest(id):
    contest = Contest.query.filter_by(id=id).first()
    if contest is None:
        flash('Invalid contest.')
        return redirect(url_for('.indexContest'))
    page = request.args.get('page', 1, type=int)
    pagination = contest.Contest_problems.paginate(
        page, per_page=current_app.config['FLASKY_AC_PROBLEM_PER_PAGE'],
        error_out=False)
    problem = [{'problem': item.Problem, 'AC_time': item.Add_time}
               for item in pagination.items]
    return render_template('contest.html', contest=contest, title="Contest",
                           endpoint='.contest', pagination=pagination,
                           problem=problem, id=id)

