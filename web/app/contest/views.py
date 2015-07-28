from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from flask.ext.login import login_required, current_user
from .forms import AddContestForm, StatusFilter, AddContestProblemForm, SubmitForm, StatusFilter, ProblemFilter
from ..models import Contest, Problem, Problem_detail, Code_detail, Contest, Contest_Problem, OJ_Status, User
from .. import db
from . import contest
from poj_submit import Submit
from poj_login import TryLogin
from poj_status import GetStatus

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
	contest = Contest.query.filter_by(id=contest_id).first()
	if contest is None:
		flash('Invalid contest.')
		return redirect(url_for('.indexContest'))
	contest_problem=contest.Contest_problems.filter_by(Contest_id=contest_id)
	problem=[]
	for values in contest_problem:
		in_problem=Problem.query.filter_by(SID=values.problems_SID).first()
		problem.append(in_problem)
	delete_SID = request.args.get('delete', -1, type=int)
	if delete_SID!=-1:
		print '-------------'
		contest.delete_problem(delete_SID)
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


@contest.route('/contest_status', methods=['GET', 'POST'])
def contest_status():
    page = request.args.get('page', 1, type=int)
    user = request.args.get('user', '')
    Result = request.args.get('result', '')
    PID = request.args.get('PID', -1, type=int)
    Contest_ID = request.args.get('Contest_id', -1, type=int)
    form=StatusFilter()
    contest = Contest.query.filter_by(id=Contest_ID).first()
    if contest is None:
        flash('Invalid contest.')
        return redirect(url_for('.indexContest'))
    contest_problem=contest.Contest_problems.filter_by(Contest_id=Contest_ID)
    problem=[]
    for values in contest_problem:
        in_problem=Problem.query.filter_by(SID=values.problems_SID).first()
        problem.append(in_problem)
    if form.validate_on_submit():
        next='/contest/contest_status?user='+form.user.data+'&result='+str(form.Result.data)+'&PID='+str(form.PID.data)+'&Contest_id='+str(Contest_ID)
        return redirect(next)
    print Contest_ID
    if user=='' and Result=='' and PID==-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID).order_by(Code_detail.RunID.desc()).paginate(
     	 page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
			error_out=False)
    elif user!='' and Result=='' and PID==-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.user==user).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif user=='' and Result!='' and PID==-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.Result==Result).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif user=='' and Result=='' and PID!=-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.PID==PID).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif user!='' and Result!='' and PID==-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.user==user,Code_detail.Result==Result).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif user!='' and Result=='' and PID!=-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.user==user,Code_detail.PID==PID).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif user=='' and Result!='' and PID!=-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.Result==Result,Code_detail.PID==PID).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif user=='':
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID,Code_detail.Result==Result,Code_detail.PID==PID).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif Result=='':
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.user==user,Code_detail.PID==PID).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
				error_out=False)
    elif PID==-1:
        pagination = Code_detail.query.filter(Code_detail.Contest_ID==Contest_ID, Code_detail.user==user,Code_detail.Result==Result).order_by(Code_detail.RunID.desc()).paginate(
    	 	  page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    	 	  	error_out=False)
    status = pagination.items
    if PID!=-1:
        form.PID.data=str(PID)
    form.user.data =user
    form.Result.data = Result
    return render_template('contest/contest_status.html',Contest_id=Contest_ID,form=form, problem=problem, status=status, pagination=pagination)

@contest.route('/contest_submit/<int:Contest_id>', methods=['GET', 'POST'])
@login_required
def contest_submit(Contest_id):    
	PID = request.args.get('PID', -1, type=int)
	form = SubmitForm()
	contest = Contest.query.filter_by(id=Contest_id).first()
	if contest is None:
		flash('Invalid contest.')
		return redirect(url_for('.indexContest'))
	contest_problem=contest.Contest_problems.filter_by(Contest_id=Contest_id)
	problem=contest_problem.count()
	user = User.query.filter_by(username=current_user.username).first()
	code=Code_detail()
	if problem>=PID:
		form.OJ_ID.data=Problem.query.filter_by(SID=contest_problem[(PID-1)].problems_SID).first().OJ_ID
	if form.validate_on_submit():
		PID=int(form.PID.data)
		if form.OJ_ID.data=='POJ':
			if user.account_POJ=='NU LL':
				flash('You need to give us your poj info first.')
				return redirect(url_for('auth.OnlineJudge'))
		code.SID=contest_problem[(PID-1)].problems_SID
		code.user=current_user.username
		code.OJ_ID=form.OJ_ID.data
		code.PID=Problem.query.filter_by(SID=contest_problem[PID-1].problems_SID).first().PID
		code.Result='Pending'
		code.Memory=''
		code.Time=''
		code.CEfile=''
		code.RemoteID=''
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
		code.Contest_ID=Contest_id
		db.session.add(code)
		db.session.commit()
		flash('Your code has been submitted.')
		fp= open('./app/main/POJcode/POJ_'+str(code.RemoteID),"w")
		fp.write(form.Code.data)
		fp.close()
		if code.Result=='Accepted':
			problem=Problem.query.filter_by(SID=code.SID).first()
			current_user.add_accepted_problem(problem)
		return redirect(url_for('contest.contest_status',Contest_id=Contest_id))
	if PID!=-1:
		form.PID.data=PID
	return render_template('contest/contest_submit.html', form=form)

@contest.route('/contest/<int:Contest_id>/contest_problem/<int:Num>', methods=['GET', 'POST'])
def contest_problem(Contest_id, Num):
	contest_problem=Contest_Problem.query.filter_by(Contest_id=Contest_id)
	num = 1;
	flag = 0
	for contest_problem in contest_problem:
		if num == Num - 1:
			SID = contest_problem.problems_SID
			flag = 1
			break
		num = num + 1
	if flag == 0:
		flash('wrong contest problem id')
		return redirect(url_for('contest.contest', id = Contest_id))
	print SID
	problem = Problem.query.get_or_404(SID)
	problems=Problem_detail()
	problems.SID=problem.SID
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
	return render_template('contest/contest_problem.html',problems=problems,num=num ,Contest_id=Contest_id)

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
    problem = [{'problem': item.Problem, 'Add_time': item.Add_time}
               for item in pagination.items]
    return render_template('contest.html', contest=contest, title="Contest",
                           endpoint='.contest', 
                           pagination=pagination,
                           problem=problem, id=id)
