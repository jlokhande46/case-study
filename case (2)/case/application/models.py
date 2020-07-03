from flask_sqlalchemy import SQLAlchemy
from application import app
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)
class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),nullable=False)
	password=db.Column(db.String(20),nullable=False)

	def __repr__(self):
		return self.username

class Patient(db.Model):
	patient_id=db.Column(db.Integer,primary_key=True)
	patient_name=db.Column(db.String(20))
	patient_age=db.Column(db.String(20))
	patient_ssn=db.Column(db.Integer)
	doa=db.Column(db.String(20))
	bed=db.Column(db.String(20))
	address=db.Column(db.String(40))
	state=db.Column(db.String(20))
	city=db.Column(db.String(20))
	status=db.Column(db.String(20))


	def __repr__(self):
		return self.patient_name

db.create_all()


 
 
			 



			 
						