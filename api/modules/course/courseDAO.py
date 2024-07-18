from db_config.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import post_dump,fields
from ..teacher.teacherDAO import TeacherModel


class CourseModel(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable = False,unique =True)
    fees = db.Column(db.Integer,nullable=False)
    conductDays = db.Column(db.String,nullable= False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    startTime =db.Column(db.String,nullable=False)
    endTime =db.Column(db.String,nullable=False)
    social_link = db.Column(db.String,nullable=False)
    duration = db.Column(db.Integer)
    is_valid = db.Column(db.Boolean,default=True)

    teacher = db.relationship('TeacherModel', backref=db.backref('course', lazy=True))
    course = db.relationship('StudentEnrolled', backref=db.backref('course', lazy=True))

# class CourseSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = CourseModel
#         fields = ("name", "fees","conductDays","teacher_id","startTime","endTime","duration")

# course_schema = CourseSchema(many=True)

class CourseSchema(SQLAlchemyAutoSchema):
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {key: value for key, value in data.items() if value is not None}

    class Meta:
        model = CourseModel
        load_instance = True
        fields = ("name", "fees", "conductDays", "teacher_id", "startTime", "endTime", "duration")

course_schema = CourseSchema(many=True)
