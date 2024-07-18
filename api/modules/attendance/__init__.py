from loguru import logger
from .controller import AddMonthlyAttendance

def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/attendance'
    logger.info(pth)
    api.add_resource(AddMonthlyAttendance, pth)