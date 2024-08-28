from loguru import logger
from .controller import AddTeacher

def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/teacher'
    logger.info(pth)
    api.add_resource(AddTeacher, pth)
    