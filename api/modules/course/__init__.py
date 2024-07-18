from loguru import logger
from .controller import AddCourse

def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/course'
    logger.info(pth)
    api.add_resource(AddCourse, pth)
    