from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import login_required, current_user
from datetime import datetime
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, SubmitForm
from .. import db
from ..models import Permission, Role, User, Problem, Problem_detail, Code_detail
from ..decorators import admin_required
from poj_submit import Submit
from poj_login import TryLogin
from poj_status import GetStatus
import sys
import os
import codecs


@main.route('/statu')
def indexStatu():
	page = request.args.get('page', 1, type=int)
	pagination = Code_detail.query.order_by(Code_detail.SID.desc()).paginate(
       page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
		error_out=False)
	status = pagination.items
	return render_template('indexStatu.html', status=status, pagination=pagination)

@main.route('/problem')
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

@main.route('/submit/<PID>/<OJ_ID>', methods=['GET', 'POST'])
@login_required
def submit(OJ_ID,PID):
	form = SubmitForm()
	user = User.query.filter_by(username=current_user.username).first()
	code=Code_detail()
	if form.validate_on_submit():
		code.user=current_user.username
		code.OJ_ID=form.OJ_ID.data
		code.PID=form.PID.data
		code.Result='Pending'
		code.Memory=''
		code.Time=''
		code.CEfile=''
		if form.Language.data=='0':
			code.Language='G++'
		if form.Language.data=='1':
			code.Language='GCC'
		if form.Language.data=='2':
			code.Language='Java'
		if form.Language.data=='3':
			code.Language='Pascal'
		if form.Language.data=='4':
			code.Language='C++'
		if form.Language.data=='5':
			code.Language='C'
		if form.Language.data=='6':
			code.Language='Fortran'
		code.Code_Length=len(form.Code.data)
		#code.Submit_Time=datetime.utcnow
		TryLogin(user.account_POJ,user.password_POJ)
		Submit(form.Code.data,code.PID,int(form.Language.data))
		code=GetStatus(current_user.account_POJ,code,form.Language.data)
		db.session.add(code)
		flash('Your code has been submitted.')
		return redirect(url_for('.indexStatu'))
	form.OJ_ID.data=OJ_ID
	form.PID.data=PID
	return render_template('submit.html', form=form)

@main.route('/problem/<int:SID>')
def problem(SID):
	problem = Problem.query.get_or_404(SID)
	problems=Problem_detail()
	problems.OJ_ID=problem.OJ_ID
	problems.PID=0
	problems.Title=''
	problems.Time_Limit=''
	problems.Memory_Limit=''
	problems.Total_Submissions=0
	problems.Accepted=0
	problems.Spical_Judge=''
	problems.Description=[]
	problems.Input=[]
	problems.Output=[]
	problems.Sample_Input=[]
	problems.Sample_Output=[]
	problems.Hint=[]
	problems.Source=''
	fp= open('./app/main/POJ/POJ_'+str(problem.PID),"r")
	arr=fp.readlines()
	flag=0
	for lines in arr:
		#print lines
		#print repr(lines)
		if lines.find('-PID-')!=-1:
			flag=1;
		elif lines.find('-Title:-')!=-1:
			flag=2;
		elif lines.find('-Time Limit:-')!=-1:
			flag=3;
		elif lines.find('-Memory Limit:-')!=-1:
			flag=4;
		elif lines.find('-Total Submissions:-')!=-1:
			flag=5;
		elif lines.find('-Accepted:-')!=-1:
			flag=6;
		elif lines.find('-Description:-')!=-1:
			flag=7;
		elif lines.find('-Input:-')!=-1:
			flag=8;
		elif lines.find('-Output:-')!=-1:
			flag=9;
		elif lines.find('-Sample Input:-')!=-1:
			flag=10;
		elif lines.find('-Sample Output:-')!=-1:
			flag=11;
		elif lines.find('-Hint:-')!=-1:
			flag=12;
		elif lines.find('-Source:-')!=-1:
			flag=13;
		elif flag==1 and lines.find('-PID-')==-1:
			problems.PID=problems.PID+int(lines)
		elif flag==2 and lines.find('-Title:-')==-1:
			problems.Title=problems.Title+lines.decode('utf-8')
		elif flag==3 and lines.find('-Memory Limit:-')==-1:
			problems.Time_Limit=problems.Time_Limit+lines
		elif flag==4 and lines.find('-Total Submissions:-')==-1:
			problems.Memory_Limit=problems.Memory_Limit+lines
		elif flag==5 and lines.find('-Accepted:-')==-1:
			lines=lines.strip()
			problems.Total_Submissions=problems.Total_Submissions+int(lines)
		elif flag==6 and lines.find('Special Judge')!=-1:
			problems.Special_Judge='Special Judge'
		elif flag==6 and lines.find('-Description:-')==-1:
			lines=lines.strip()
			problems.Accepted=problems.Accepted+int(lines)
		elif flag==7 and lines.find('-Input:-')==-1:
			problems.Description.append(lines.decode('utf-8'))
		elif flag==8 and lines.find('-Output:-')==-1:
			problems.Input.append(lines.decode('utf-8'))
		elif flag==9 and lines.find('-Sample Input:-')==-1:
			problems.Output.append(lines.decode('utf-8'))
		elif flag==10 and lines.find('-Sample Output:-')==-1:
			problems.Sample_Input.append(lines.decode('utf-8'))
		elif flag==11 and lines.find('-Hint:-')==-1:
			problems.Sample_Output.append(lines.decode('utf-8'))
		elif flag==12 and lines.find('-Source:-')==-1:
			problems.Hint.append(lines.decode('utf-8'))
		elif flag==13:
			problems.Source=problems.Source+lines.decode('utf-8')+'\n'
	fp.close()
	return render_template('problem.html',problems=problems)
	 

