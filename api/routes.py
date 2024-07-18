from flask_restful import Api
# from flask_restful import Resource
from modules.course import routes as add_course_route
from modules.student import routes as add_student_route
from modules.teacher import routes as add_teacher_route
from modules.Registration import routes as add_registration_route
class Routes(object):
    def __init__(self, app, base_path):
        self.api = Api(app)
        self.base_path = base_path
        
        add_course_route(self.api, self.base_path)
        add_student_route(self.api, self.base_path)
        add_teacher_route(self.api,self.base_path)
        add_registration_route(self.api,self.base_path)
