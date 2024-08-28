from loguru import logger
from .controller import PayRegFees

def routes(api, base_path):
    pth = ''.join(base_path)
    pth = base_path+'/bookSeat'
    logger.info(pth)
    api.add_resource(PayRegFees, pth)
