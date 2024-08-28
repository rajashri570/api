from db_config.database import db
from datetime import datetime, date
import calendar

class StudentModel(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable = False)
    address = db.Column(db.String)
    contact = db.Column(db.String,nullable= False)
    email =db.Column(db.String,nullable=False)
    passwd =db.Column(db.String,nullable=False)
    is_valid = db.Column(db.Boolean,default=True)
    
class StudentEnrolled(db.Model):
    __tablename__ = 'studentenrolled'
    id = db.Column(db.Integer, primary_key=True)
    studId=db.Column(db.Integer,db.ForeignKey('student.id'))
    courseId = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    feesPaidSatus = db.Column(db.Boolean,default=False)
    joindate = db.Column(db.Date, default=date.today)


def get_last_day_of_current_month():
    today = datetime.today()
    last_day = calendar.monthrange(today.year, today.month)[1]  
    return datetime(today.year, today.month, last_day)

class FeesPaymentModel(db.Model):
    __tablename__= 'feespayment'
    id = db.Column(db.Integer, primary_key=True)
    StudId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    courseId = db.Column(db.Integer,db.ForeignKey('course.id'))
    amount = db.Column(db.Float,nullable=False)
    payStatus =db.Column(db.Boolean)
    transaction_id  = db.Column(db.String(100), unique=True, nullable=False)
    month = db.Column(db.String,nullable= False)
    dueDate = db.Column(db.Date,default=get_last_day_of_current_month)
    paymentDate = db.Column(db.Date,default=datetime.today)