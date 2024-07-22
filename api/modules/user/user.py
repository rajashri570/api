from .userDAO import UserModel
from db_config.database import db
from common.response import *
from loguru import logger
class User(UserModel):
    def save(self,username,password,role,createdDate):
        try:
            userObj = UserModel(username=username, password=password, role=role, createdDate=createdDate)
            db.session.add(userObj)
            db.session.commit()
            return Response(
                ResponseEnum.Success,message="User created Successfully!!!",data={"id":userObj.id}    
            )

        except Exception as e:
            logger.exception({str(e)})
            db.session.rollback()
            return Response(
                ResponseEnum.Failed,message="Error while adding user!!"
            )