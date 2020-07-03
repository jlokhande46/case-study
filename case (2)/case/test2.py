from application import app
from flask import render_template, flash, redirect, url_for, request, session
from application.models import db, User
from application.forms import LoginForm
app.secret_key="hello"
flag=0
@app.route('/',methods=["POST","GET"])
@app.route('/login',methods=["POST","GET"])
def login():
	form= LoginForm()
	session["user"]=False
	if form.validate_on_submit():
		value=form.username.data
		pw=form.password.data
		valid=User.query.filter_by(username=value).first()
		password=User.query.filter_by(password=pw).first()
		if valid and password:
			session["user"]=True
			return redirect(url_for("exe"))
		else:
			flash("Invalid username or password")
			return render_template("login.html", form=form)	
	return render_template("login.html", form=form)
@app.route('/exe',methods=["POST","GET"])
def exe():
	if request.method=="POST":
		if request.form.get('Patient'):
			if request.form.get('Patient')=="View":
				return render_template("add_patient.html")
			if request.form.get('Patient')=="Delete":
				return render_template("delete_p.html")
			if request.form.get('Patient')=='Update':
				return render_template('update_p.html')
		if request.form.get('submit'):
			return "added you"		

	if session["user"]:
		session["user"]=False
		return render_template("add_patient.html")

		  	 	
	return redirect(url_for('login'))


@app.route("/test",methods=["POST","GET"])
def test():
	if request.method=="POST":
		if request.form.get('m'):
			if request.form.get('m')=="redirect":
				return "hello" 
		if request.form.get('m'):
			return "age"	
	return render_template("test.html")