from flask import  request,jsonify
from flask_jwt_extended import (get_jwt)
from flask_jwt_extended import get_jwt_identity,jwt_required
from flask_restful import Resource

from .business import BusinessFun,MappingFun

class CreateBusiness(Resource):
    @jwt_required()
    def post(self):
        try:
            print("ggg")
            # id = get_jwt_identity()
            user_role = get_jwt()['roles']
            print(user_role)
            # Check if the user has the 'admin' role
            if user_role != 'admin':
                return jsonify(message="Unauthorized access")
                # return {
                #     'message':'Unauthorized access'
                # },401
            body = request.get_json()
            print(body)
            
            newbusines =BusinessFun()
            result = newbusines.save(body)
            return jsonify(message= result)
        except Exception as e:
            print(f"kkkkkk {e}")
           
            

class User_Busines_Mapper(Resource):
    def post(self):
        try:
            body = request.get_json()
            print(body)

            newmap =MappingFun()
            result = newmap.save(body)
            return jsonify(message= result)
        except Exception as e:
            print(f"kkkkkk {e}")
             
    
class Business_login(Resource):
    @jwt_required()
    def post(self):
        try:
            print("inside busines login")
            id = get_jwt_identity()
            print(id)
            # return jsonify({"id---":id})
            header=get_jwt()
            # return "ok"
            obj =MappingFun()
            result = obj.login(id,header)
            return jsonify(message= result)
        except Exception as e:
            print(f"kkkkkk {e}")
            # return jsonify({"error": "An error occurred while processing your request"}), 500
            return "mno"

        #     body = request.get_json()
        #     print(body)

        #     newmap =MappingFun()
        #     result = newmap.login(body)
        #     # print(result)
        #     return jsonify(message= result)
        # except Exception as e:
        #     print(f"Error: {e}")
        #     return "Error....."




# class Business_login(Resource):
#     @jwt_required()
#     def post(self):
#         try:
#             return "hello"
#         except:
            # return "not"