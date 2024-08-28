
from flask_restful import Resource
from flask import request
from common.response import *
from .registor import Registor
from loguru import logger
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from ..student.studentDAO import StudentModel

class PayRegFees(Resource):
    @jwt_required()
    def post(self):
        try:
            # body = request.json()
            current_stud = get_jwt_identity()
            record = StudentModel.query.filter_by(id=current_stud).first()

            body = request.get_json()
            amount = body['amount']
            obj = Registor()
            result = obj.save(current_stud,amount)
            if result.status == ResponseEnum.Success:
                return {"status":"Success","message":result.message,"data":result.data},201
            else:
                 return {"status":"failed","message":"Error while paying fees!"}
        except Exception as e:
            logger.exception(f"{str(e)}")
            return {"status":"Failed","message":"Internal server error"},505
 
        

