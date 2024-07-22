from flask_restful import Resource
from flask import request
import datetime as d
from common.response import *
from loguru import logger

class AddUser(Resource):
    def post(self):
        try:
            from .user import User
            body = request.get_json()
            username = body['username']
            password =body['password']
            role = body['role']
            createdDate1 = body['createdDate']
            createdDate = d.datetime.strptime(createdDate1, '%d-%m-%Y').date()
            print(createdDate)
            obj = User()
            result = obj.save(username,password,role,createdDate)
            if result.status == ResponseEnum.Success:
                    return {"status":"Success","message":result.message,"data":result.data},201
        except Exception as e:
            logger.exception(f"{str(e)}")
            return {"status":"Failed","message":"Internal server error"},505






