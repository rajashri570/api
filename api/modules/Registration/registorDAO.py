from db_config.database import db
import datetime as dt

class RegistorModel(db.Model):
    __tablename__ = 'registor'
    id = db.Column(db.Integer, primary_key=True)
    studId = db.Column(db.Integer,nullable = False)
    amount = db.Column(db.Integer,nullable = False)
    paidDate = db.Column(db.Date)
    feesPaidStatus = db.Column(db.Boolean,default=False)

