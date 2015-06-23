from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import current_user
from .forms import AddContestForm
from ..models import Contest
from .. import db
from . import contest

@contest.route('/add_contest', methods=['GET', 'POST'])
def add_contest():
    form = AddContestForm()
    if form.validate_on_submit():
        contest = Contest(Title=form.Title.data, 
                    #Begin_time=form.Begin_Time.date,
                    #End_time=form.End_Time.date,
                    Manager=current_user.username)
        db.session.add(contest)
        flash('The contest has been added.')
        return redirect(url_for('main.index'))
    return render_template('add_contest.html', form=form)
