from .controller import CreateUser
from .controller import LoginUser
from .controller import CheckBusiness
# from .controller import ListAllUsers
from loguru import logger

def routes(api,base_path):
    # pth=''.join(base_path)
    pth = base_path+'/user'
    logger.info(pth)
    api.add_resource(CreateUser,pth+'/add')
    
    api.add_resource(LoginUser,pth+'/login')
    api.add_resource(CheckBusiness,pth+'/check_business')
    # api.add_resource(ListAllUsers,pth+'/allusers')
