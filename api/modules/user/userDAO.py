from db_config.database import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,nullable = False)
    password = db.Column(db.String,nullable = False)
    role = db.Column(db.String,nullable=False)
    createdDate = db.Column(db.DateTime)
       
 