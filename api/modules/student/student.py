from .studentDAO import StudentModel,StudentEnrolled,FeesPaymentModel
from .studentDAO import get_last_day_of_current_month
from db_config.database import db
from common.response import *
from loguru import logger
from datetime import datetime
from datetime import date 
from ..user.userDAO import UserModel
from ..course.courseDAO import CourseModel,course_schema
from flask_jwt_extended import create_access_token
from service.email.email import MailServer
# from flask import current_app as app

class Student(StudentModel):
    
    def save(self,body):
        try:
            email = body.get('email')
            passwd = body.get('passwd')
            name = body.get('name')

            # student is already present
            studrecord = StudentModel.query.filter_by(email=email,name=name).first()  
            if studrecord:
                return Response(
                ResponseEnum.Success,message = "Student record is already present...!"
            )       
            obj = StudentModel(**body)
            db.session.add(obj)
            db.session.commit()
            # add here code to check student exist already.
           
            if email and passwd:
                today = date.today()
                print(today)
                user = UserModel(
                    username=email,
                    password=passwd,
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
            record = StudentEnrolled.query.filter_by(studId=loggedStudId,courseId=courseid).first()
            if record:
                return Response(
                ResponseEnum.Success,message = "You have already enrolled for this course!!")
            
            obj = StudentEnrolled(studId=loggedStudId,courseId=courseid,feesPaidSatus=status)
            print({"id":obj.id,
                   "courseid":obj.courseId,
                   "feesPaidSatus":obj.feesPaidSatus})
            db.session.add(obj)
            db.session.commit()

            

            studObj = Student.query.filter_by(id=loggedStudId).first()
            print("EMail.............",studObj.email)

            courseObj = CourseModel.query.filter_by(id=courseid).first()
            email = MailServer()
            
            # email.send_mail("preetheshks21@gmail.com","/ggoglemeet")
            email.send_mail(studObj.email,courseObj.social_link)

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
            
            StudId =body['StudId']
            courseId= body['courseId']
            month= body['month']
            paydate = body['paymentDate'] 
            # paymentdt = datetime.strptime(paydate, "%Y-%m-%d")
            # due_date = get_last_day_of_current_month()
            
            feesrec = FeesPaymentModel.query.filter_by(StudId=StudId, courseId=courseId, month=month).first()
            
            if feesrec:
                    return Response(
                ResponseEnum.Success,message ="You have aleady done payment for given month and course"
            )
            obj = FeesPaymentModel(**body)
            db.session.add(obj)
            db.session.commit()
            return Response(
                ResponseEnum.Success,message ="paid fees successfully!!!"
            )
        
        except Exception as e:
            logger.exception(f"{str(e)}")
            db.session.rollback()
            raise e


            




    
        