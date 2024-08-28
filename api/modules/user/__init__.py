from loguru import logger
from .controller import AddUser

def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/User'
    logger.info(pth)
    api.add_resource(AddUser, pth)