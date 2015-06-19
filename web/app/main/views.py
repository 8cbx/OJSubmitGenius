from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import Permission, Role, User, Problem, Problem_detail
from ..decorators import admin_required
import sys
import os
import codecs

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
	problems=Problem_detail()
	problems.PID=''
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
		print lines
		print repr(lines)
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
			problems.PID=problems.PID+lines
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
	 

