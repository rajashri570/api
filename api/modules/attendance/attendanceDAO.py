
from db_config.database import db

class AttendanceModel(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)  # True for present, False for absent

    user = db.relationship('StudentModel', backref=db.backref('attendance', lazy=True))