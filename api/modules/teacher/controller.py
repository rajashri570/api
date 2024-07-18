from flask_restful import Resource
from flask import request
from loguru import logger
from common.response import *
from .teacher import Teacher

class AddTeacher(Resource):
    def post(self):
        try:
            body = request.get_json()
            obj = Teacher()
            result = obj.save(body)
            if result.status == ResponseEnum.Success:
                    return {"status":"Success","message":result.message},201
        except Exception as e:
            logger.exception(f"{str(e)}")
            return {"status":"Failed","message":"Internal server error"},505

