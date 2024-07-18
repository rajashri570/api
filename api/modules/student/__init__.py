from loguru import logger
from .controller import AddStudent,LoginStudent
from .controller import EnrollStudCourse,ViewCourse
def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/student'
    logger.info(pth)
    api.add_resource(AddStudent, pth)
    api.add_resource(ViewCourse,pth+'/viewCourses')
    api.add_resource(LoginStudent,pth+'/login')
    api.add_resource(EnrollStudCourse,pth+'/register')
    