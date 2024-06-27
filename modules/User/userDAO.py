from sqlalchemy.sql.sqltypes import BIGINT
from db_config.database import db
from sqlalchemy import FetchedValue

class User(db.Model):
    id = db.Column('id',BIGINT, primary_key=True,unique=True, nullable=False)
    first_name = db.Column('first_name',db.String)
    last_name = db.Column('last_name',db.String)
    mobile = db.Column('mobile',db.String)
    email = db.Column('email',db.String)
    role = db.Column('role',db.String)
    passwd = db.Column('passwd', db.String(128))

    delete_status=db.Column('delete_status',db.Boolean,nullable=False,server_default=FetchedValue())
    
    # User_business_mapper = db.relationship('User_business_mapper', backref='bars_bar')
    
