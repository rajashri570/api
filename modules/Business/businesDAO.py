from sqlalchemy.sql.sqltypes import BIGINT
from db_config.database import db
from sqlalchemy import ForeignKey

from sqlalchemy import FetchedValue

class Business(db.Model):
    # __tablename__ = 'business'
    id = db.Column('id',BIGINT, primary_key=True,unique=True, nullable=False)
    bname = db.Column('bname',db.String)
    baddr = db.Column('baddr',db.String)
    
    contact = db.Column('contact',db.Integer)
    email = db.Column('email',db.String)
    delete_status=db.Column('delete_status',db.Boolean,nullable=False,server_default=FetchedValue())
    __table_args__ = {'extend_existing': True}
   

class LinkUserBusiness(db.Model):
    __tablename__ = 'LinkUserBusiness'
    id = db.Column('id',BIGINT, primary_key=True,unique=True, nullable=False,autoincrement=True)
    # uid = db.Column('uid', db.Integer)
    # bid = db.Column('bid', db.Integer)
    uid = db.Column('uid', BIGINT, ForeignKey('user.id'), nullable=False)
    bid = db.Column('bid', BIGINT, ForeignKey('business.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    delete_status=db.Column('delete_status',db.Boolean,nullable=False,server_default=FetchedValue())
    user = db.relationship('User', backref=db.backref('link_user_businesses', lazy=True))
    business = db.relationship('Business', backref=db.backref('link_user_businesses', lazy=True))
    __table_args__ = {'extend_existing': True}
   
    
    
    

    