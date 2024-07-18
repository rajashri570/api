from .studentDAO import StudentModel,StudentEnrolled,FeesPaymentModel
from db_config.database import db
from common.response import *
from loguru import logger
import datetime as dt
from ..user.userDAO import UserModel
from ..course.courseDAO import CourseModel,course_schema
from flask_jwt_extended import create_access_token



# from flask_bcrypt import Bcrypt 

class Student(StudentModel):
    def save(self,body):
        try:
            obj = StudentModel(**body)
            db.session.add(obj)
            # db.session.commit()
            # add here code to check student exist already.
            email = body.get('email')
            password = body.get('passwd')
            if email and password:
                today = dt.date.today()
                print(today)
                user = UserModel(
                    username=email,
                    password=password,
                    role='student',
                    createdDate = today
                )
                print(user)
                db.session.add(user)
                db.session.commit()
            return Response(
                ResponseEnum.Success,message = "Student added successfully!!"
            )
        except Exception as e:
            logger.exception({str(e)})
            db.session.rollback()
            return Response(
                ResponseEnum.Failed,message="Error while adding student!!"
            )
   
    def login(self,body):
        try:
            email = body['email']
            passwd = body['passwd']
            print(email,passwd)
            record = db.session.query(StudentModel).filter_by(email=email, passwd=passwd).first()
            if record:
                access_token = create_access_token(identity=record.id)
                return Response(
                ResponseEnum.Success,message = "Student logged in successfully!!",data=access_token
            )
            else:
                return Response(
                ResponseEnum.Success,message = "Invalid Credentials!!"
            )
        except Exception as e:
            logger.exception(f"{str(e)}")
            raise e
        
   
    def enroll_stud_course(self,loggedStudId,courseid,status):
        try:
           
            obj = StudentEnrolled(id=loggedStudId,courseId=courseid,feesPaidSatus=status)
            print({"id":obj.id,
                   "courseid":obj.courseId,
                   "feesPaidSatus":obj.feesPaidSatus})
            db.session.add(obj)
            db.session.commit()

        
            return Response(
                ResponseEnum.Success,message = "successfully enrolled for course!!"
            )

        except Exception as e:
            logger.exception(f"{str(e)}")
            raise e


    def view_all_courses(self):
        try:
            records = CourseModel.query.with_entities(
                    CourseModel.name, 
                    CourseModel.fees, 
                    CourseModel.conductDays, 
                    CourseModel.teacher_id, 
                    CourseModel.startTime, 
                    CourseModel.endTime, 
                    CourseModel.duration
                ).all()

            if not records:
                return Response(
                        ResponseEnum.Success, data=[]
                    )

            result = course_schema.dump(records)
            return Response(
                    ResponseEnum.Success, data=result
                )
                
        except Exception as e:
                logger.exception(f"{str(e)}")
                raise e
        
    def pay_fees(self,body):
        try:

            obj = FeesPaymentModel(**body)
            db.session.add(obj)

            return Response(
                ResponseEnum.Success,message = "successfully enrolled for course!!"
            )

        except Exception as e:
            logger.exception(f"{str(e)}")
            db.session.rollback()
            raise e


            




    
        