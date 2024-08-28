from loguru import logger
from .controller import AddCourse,GetEnrolledStudents

def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/course'
    logger.info(pth)
    api.add_resource(AddCourse, pth)
    api.add_resource(GetEnrolledStudents,pth)


    