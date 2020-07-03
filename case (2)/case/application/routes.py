from application import app
from flask import render_template, flash, redirect, url_for, request, session
from application.models import db, User, Patient
from application.forms import LoginForm
app.secret_key="hello"
 
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

#exectuive opens and redirect to respective buttons on it acc to functions
@app.route('/exe',methods=["POST","GET"])
def exe(): 
	if session["user"]:
		return redirect(url_for("add_patient"))   	 	
	return redirect(url_for('login'))

#test this is only for testing purpose. no use 
@app.route("/test",methods=["POST","GET"])
def test():
	if request.method=="POST":
		if request.form.get('m'):
			if request.form.get('m')=="redirect":
				return "hello" 
		if request.form.get('m'):
			return "age"	
	return render_template("test.html")

#executive functions


@app.route('/add_patient',methods=["POST","GET"])
def add_patient():
	if request.method=="POST":
		if request.form.get('Patient'):
			if request.form.get('Patient')=="Patient":
	 			session["Patient"]=True
	 			return redirect(url_for('add_patient'))
			if request.form.get('Patient')=="Search":
				session["Patient"]=True
				return redirect(url_for('search_patient'))
			if request.form.get('Patient')=="View":
				session["Patient"]=True
				return redirect(url_for("view_patient"))
			if request.form.get('Patient')=="Delete":
				session["Patient"]=True
				return redirect(url_for("delete_patient"))
			if request.form.get('Patient')=='Update':
				session["Patient"]=True
				return redirect(url_for("update_patient"))

		if request.form.get('submit'):
			a=Patient(patient_name=request.form.get('pname'),patient_age=request.form.get('age'),patient_ssn=request.form.get('ssnid'),doa=request.form.get('date'),bed=request.form.get('bedtype'),address=request.form.get('address'),state=request.form.get('state'),city=request.form.get('city'),status='active')
			db.session.add(a)
			db.session.commit()
			flash("patient added")
			return render_template("add_p.html")

	if session["user"]:
		session["user"]=False
		flash("you are logged in as executive")
		return render_template("add_p.html")

	if "Patient" in session:
		if session["Patient"]:
			session["Patient"]=False
			return render_template("add_p.html")
	return redirect(url_for('login'))




@app.route('/view_patient',methods=["POST","GET"])
def view_patient(): 
	if request.method=="POST":
		if request.form.get('Patient'):
			if request.form.get('Patient')=="Patient":
	 			session["Patient"]=True
	 			return redirect(url_for('add_patient'))
			if request.form.get('Patient')=="Search":
				session["Patient"]=True
				return redirect(url_for('search_patient'))
			if request.form.get('Patient')=="View":
				session["Patient"]=True
				return redirect(url_for("view_patient"))
			if request.form.get('Patient')=="Delete":
				session["Patient"]=True
				return redirect(url_for("delete_patient"))
			if request.form.get('Patient')=='Update':
				session["Patient"]=True
				return redirect(url_for("update_patient"))
	if "Patient" in session:
		if session["Patient"]:
			session["Patient"]=False
			data=Patient.query.all()
			return render_template("view_p.html",data=data)
	return redirect(url_for('login'))



@app.route('/delete_patient',methods=["POST","GET"])
def delete_patient():
	if request.method=="POST":
		if request.form.get('Patient'):
			if request.form.get('Patient')=="Patient":
	 			session["Patient"]=True
	 			return redirect(url_for('add_patient'))
			if request.form.get('Patient')=="Search":
				session["Patient"]=True
				return redirect(url_for('search_patient'))
			if request.form.get('Patient')=="View":
				session["Patient"]=True
				return redirect(url_for("view_patient"))
			if request.form.get('Patient')=="Delete":
				session["Patient"]=True
				return redirect(url_for("delete_patient"))
			if request.form.get('Patient')=='Update':
				session["Patient"]=True
				return redirect(url_for("update_patient"))
		if request.form.get('get'):
			pid=request.form.get('ssnid')
			data=Patient.query.filter_by(patient_ssn=pid).first()
			if data:
				flash("Patient Found successfully")
				return render_template("delete_p.html",data=data)
			flash("Invalid ID or Check Patient status")
			return render_template("delete_p.html")
		if request.form.get('Delete'):
			pid=request.form.get('ssnid')
			data=Patient.query.filter_by(patient_ssn=pid).first()
			db.session.delete(data)
			db.session.commit()
			flash("Deleted Successfully")
			return render_template("delete_p.html")

	if "Patient" in session:
		if session["Patient"]:
			session["Patient"]=False
			flash("Enter 'PatientID' which you want to Delete")
			return render_template("delete_p.html")
	return redirect(url_for('login'))
	

@app.route('/update_patient',methods=["POST","GET"])
def update_patient():
	if request.method=="POST":
		if request.form.get('Patient')=="Patient":
	 			session["Patient"]=True
	 			return redirect(url_for('add_patient'))
		if request.form.get('Patient'):
			if request.form.get('Patient')=="Search":
				session["Patient"]=True
				return redirect(url_for('search_patient'))
			if request.form.get('Patient')=="View":
				session["Patient"]=True
				return redirect(url_for("view_patient"))
			if request.form.get('Patient')=="Delete":
				session["Patient"]=True
				return redirect(url_for("delete_patient"))
			if request.form.get('Patient')=='Update':
				session["Patient"]=True
				 
				return redirect(url_for("update_patient"))
		if request.form.get('get'):
			pid=request.form.get('ssnid')
			data=Patient.query.filter_by(patient_ssn=pid).first()
			if data:
				flash("Patient Found successfully.Now you can update the changes.")
				return render_template("update_p.html",data=data)
			flash("Invalid ID or Check Patient status")
			return render_template("update_p.html")	
		if request.form.get('update'):
			pid=request.form.get('ssnid')
			data=Patient.query.filter_by(patient_ssn=pid).first()
			data.patient_name=request.form.get('pname')
			data.patient_age=request.form.get('age')
			data.doa=request.form.get('date')
			data.bed=request.form.get('bedtype')
			data.address=request.form.get('address')
			data.state=request.form.get('state')
			data.city=request.form.get('city')
			db.session.commit()
			flash("updated successfully")
			return render_template("update_p.html")

	if "Patient" in session:
		if session["Patient"]:
			session["Patient"]=False
			flash("Enter Patient ID, whose changes you want to do.")
			return render_template("update_p.html")
	return redirect(url_for('login'))	

@app.route('/search_patient',methods=["POST","GET"])
def search_patient():
	if request.method=="POST":
		if request.form.get('Patient'):
			if request.form.get('Patient')=="Patient":
	 			session["Patient"]=True
	 			return redirect(url_for('add_patient'))
			if request.form.get('Patient')=="Search":
				session["Patient"]=True
				return redirect(url_for('search_patient'))
			if request.form.get('Patient')=="View":
				session["Patient"]=True
				return redirect(url_for("view_patient"))
			if request.form.get('Patient')=="Delete":
				session["Patient"]=True
				return redirect(url_for("delete_patient"))
			if request.form.get('Patient')=='Update':
				session["Patient"]=True
				return redirect(url_for("update_patient"))
		if request.form.get('submit'):
			pid=request.form.get('ssnid')
			data=Patient.query.filter_by(patient_ssn=pid).first()
			if data:
				flash("Patient Found successfully")
				return render_template("search_p.html",data=data)
			flash("Invalid ID or Check Patient status")
			return render_template("search_p.html")	

	if "Patient" in session:
		if session["Patient"]:
			session["Patient"]=False
			return render_template("search_p.html")
	return redirect(url_for('login'))	

		