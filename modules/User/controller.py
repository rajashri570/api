
from flask import  request,jsonify
# from flask_jwt_extended import (get_jwt)
from flask_restful import Resource
# from db_config import db
# from .controller import User
from db_config.database import db
from .userDAO import User
from .user import  UserFun
# from .user import Check_business
from flask_jwt_extended import jwt_required,get_jwt_identity
# from Business.business import MappingFun

class CreateUser(Resource):
    def post(self):
      
        body = request.get_json()
        print(body)
        
        newuser =UserFun()
        result = newuser.save(body)
        return jsonify({"message": result})

class LoginUser(Resource):
    def post(self):
        print("hi=================")
       
        data = request.get_json()
        # email = data.get('email')
        # password = data.get('mobile')
        print(data)
        uobj = UserFun()
    
        result = uobj.login(data)
        
        return jsonify({"mesaage":result})

        #     user = User.query.filter_by(email=email).first()
        #     if user and user.check_password(password):  # Implement check_password method in User model
        #         access_token = create_access_token(identity=user._id)
        #         return jsonify({'access_token': access_token}), 200
        #     else:
        #         return jsonify({'message': 'Invalid credentials'}), 401

        # except Exception as e:
        #     return jsonify({'message': f'Error: {str(e)}'}), 500

# # class Map_user_busines(Resource):
# class ListAllUsers(Resource):  
#    def get(self):
#        users = User.query.all()
#     #    users_list = [user.to_dict() for user in users]
#        return ({})
class CheckBusiness(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user = get_jwt_identity()
            print(current_user)
            obj = UserFun()
            result = obj.Check_business(current_user)
            return jsonify(message=result)
        except Exception as e:
            print("Error in get business logic")
            
      
        
        
      
        
