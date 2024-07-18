from flask_restful import Resource
from flask import request
from common.response import *
from loguru import logger
from .student import Student
from db_config.database import db


from flask_jwt_extended import jwt_required,get_jwt_identity,get_jwt

class AddStudent(Resource):
    def post(self):
        try:
            body = request.get_json()
            studObj = Student()
            result =studObj.save(body)
            if result.status == ResponseEnum.Success:
                    return {"status":"Success","message":result.message},201
        except Exception as e:
            logger.exception(f"{str(e)}")
            return {"status":"Failed","message":"Internal server error"},505

class LoginStudent(Resource):
    def post(self):
        try:
            body = request.get_json()
            studObj = Student()
            result = studObj.login(body)
            if result.status == ResponseEnum.Success:
                return {"status":"Success","message":result.message,"data":result.data},201
        except Exception as e:
                logger.exception(f"{str(e)}")
                return {"status":"Failed","message":"Internal server error"},505
        
     
class EnrollStudCourse(Resource):
    @jwt_required() 
    def post(self):
        try:
            print("---------------in reg controller")
            claims = get_jwt()     
            paidstatus = claims.get("feesPaidStatus")           
            loggedStudId = get_jwt_identity()
            data = request.get_json()  # Parse the incoming JSON data
            courseid = data.get('courseid')
            studObj = Student()
            result = studObj.enroll_for_course(loggedStudId,courseid,paidstatus)
            if result.status == ResponseEnum.Success:
                return {"status":"Success","message":result.message},201
        except Exception as e:
                logger.exception(f"{str(e)}")
                return {"status":"Failed","message":"Internal server error"},505
        
class ViewCourse(Resource):
     def get(self):
        try:
            obj = Student()
            result = obj.view_all_courses()
            if result.status == ResponseEnum.Success:
                return {"status":"Success","message":result.message,"data":result.data},201
        except Exception as e:
                logger.exception(f"{str(e)}")
                return {"status":"Failed","message":"Internal server error"},505
            