from .courseDAO import CourseModel
from ..teacher.teacherDAO import TeacherModel
from db_config.database import db
from common.response import *
from loguru import logger


class Course(CourseModel):
    def save(self,body):
        try:
            name = body['name']
            teacherid = body['teacher_id']
            # code for checking the duplicate course entry
            record = CourseModel.query.filter_by(name=name).first()
            if record:
                return Response(
                    ResponseEnum.Success,message="Course already added with this name!!"
                )
            
            # record to check the time slot not taken by other course
            records = CourseModel.query.all()
            for rec in records:
                if rec.startTime == body['startTime'] and rec.endTime == body['endTime']:
                    return Response(
                        ResponseEnum.Success,message=f"Sorry!! time slot {rec.startTime}:{rec.endTime} is taken already!"
                    )
                
            teacher = TeacherModel.query.get(teacherid)
            if name not in teacher.degree :
                return Response(
                        ResponseEnum.Success,message=f"Sorry!! Selected teacher is not having degree for this course"
                    )

            obj = CourseModel(**body)
            db.session.add(obj)
            db.session.commit()
            return Response(
                ResponseEnum.Success,message = "Course added successfully!!"
            )
        except Exception as e:
            logger.exception({str(e)})
            db.session.rollback()
            return Response(
                ResponseEnum.Failed,message="Error while adding Course!!"
            )
        

    
    
    
    
    
