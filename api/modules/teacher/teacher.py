from .teacherDAO import TeacherModel
from db_config.database import db
from common.response import *
from loguru import logger
from ..user.userDAO import UserModel
import datetime as dt

class Teacher(TeacherModel):
    def save(self,body):
        try:
            teacherobj = TeacherModel(**body)
            db.session.add(teacherobj)
            db.session.commit()
            email = body.get('email')
            password = body.get('passwd')
            if email and password:
                today = dt.date.today()
                print(today)
                user = UserModel(
                    username=email,
                    password=password,
                    role='teacher',
                    createdDate = today
                )
                print(user)
                db.session.add(user)
                db.session.commit()
            return Response(ResponseEnum.Success,message="Teacher created Successfully!!!",data=teacherobj.id)
        except Exception as e:
            logger.exception({str(e)})
            db.session.rollback()
            return Response(
                ResponseEnum.Failed,message="Error while adding teacher!!"
            )
