from flask_restful import Resource
from flask import request
from common.response import *


from loguru import logger

class AddCourse(Resource):
    def post(self):
        try:
            from .course import Course
            body = request.get_json()
            cobj = Course()
            result = cobj.save(body)
            if result.status == ResponseEnum.Success:
                return {"status":"Success","message":result.message},201
        except Exception as e:
            logger.exception(f"{str(e)}")
            return {"status":"Failed","message":"Internal server error"},505
 
            
class GetEnrolledStudents(Resource):
    def get(self):
        try:
            from .course import Course
            CourseId = request.args.get('id')
            cobj = Course()
            result = cobj.view_students(CourseId)
            if result.status == ResponseEnum.Success:
                return {"status":"Success","message":result.message,"data":result.data},201
        except Exception as e:
            logger.exception(f"{str(e)}")
            return {"status":"Failed","message":"Internal server error"},505

        