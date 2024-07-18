from db_config.database import db

class TeacherModel(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable = False)
    address = db.Column(db.String)
    contact = db.Column(db.String,nullable= False)
    email =db.Column(db.String,nullable=False)
    passwd =db.Column(db.String,nullable=False)
    degree = db.Column(db.String,nullable=False)
    passingYear = db.String(db.String)
    is_valid = db.Column(db.Boolean,default=True)

