from .registorDAO import RegistorModel
from db_config.database import db
from common.response import *
from loguru import logger
import datetime as dt
from flask_jwt_extended import create_access_token

class Registor(RegistorModel):
    def save(self,studId,amount):
        try:
            if amount == 500:
                status = True
                paydt = dt.date.today()

            regObj = RegistorModel(studId=studId,amount=amount,feesPaidStatus=status,paidDate=paydt)
            enroll_token = create_access_token(identity=studId,additional_claims={"feesPaidStatus":status})
            
            db.session.add(regObj)
            db.session.commit()
            return Response(
                ResponseEnum.Success,message = "registration fees paid successfully!!",data=enroll_token
            )
        except Exception as e:
            logger.exception({str(e)})
            db.session.rollback()
            raise e
                
