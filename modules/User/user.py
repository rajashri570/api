from db_config.database import db
from .userDAO import User
from modules.Business.businesDAO import LinkUserBusiness
from flask import jsonify
from flask_jwt_extended import create_access_token
# from .controller import CheckBusiness


class UserFun(User):
    def __init__(self):
        pass
    
    
    def save(self,body):
        try:
            print(body)
            new_user = User(**body)
            
            db.session.add(new_user)
            db.session.commit()
            return "User added Succcessfully!!!"
        except Exception as e:
            print(e)
            return "error"
        
    def login(self,body):
        try:
            # data = request.get_json()
            email = body.get('email')
            password = body.get('passwd')
            print("data : ",email,password)
            user = User.query.filter_by(email=email).first()
            # return user.mobile
            # print(user.passwd)
            
            if user and user.passwd==password: 
                # print("yes....")# Implement check_password method in User model
                # access_token = create_access_token(identity=user.id)
                # additional_claims = {"roles": user.role, "name": user.first_name}
                access_token = create_access_token(identity=user.id, additional_claims={"roles": user.role, "name": user.first_name})
                print(user.role)
                return f"access_token': {access_token}", 200
                # return "no"
               
            else:
                return  "error in access token generation!"

        except Exception as e:
            print(e)
            return "error"
    # place code here to check business
    
    def Check_business(self,id):
        try:
            print("in check business function!!!")
            uid = id
            rec = LinkUserBusiness.query.filter_by(uid=uid).first()
            if rec :
                return "/api/v1/business/login"
            else:
                return "/api/v1/business/CreateBusiness"
        except Exception as e:
            return "Error in checking the business...!"            
            