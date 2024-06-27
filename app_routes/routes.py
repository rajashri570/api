from flask_restful import Resource, Api
import logging as logger

# from business import routes as business_routes
# from business import routes_dealer as business_routes_dealer
# from user import routes as user_routes

from modules.User import routes as add_user_routes
from modules.Business import routes as add_busines_route

# from outlet import routes as outlet_r

class AppRoutes(object):
    def __init__(self,app,base_path=None):
         self.api=Api(app)
         self.base_path=''.join(base_path)
         logger.basicConfig(level=logger.DEBUG)  
         logger.info(f"Base path {self.base_path}")
      
    #   here i have added imported route from init.py
         add_user_routes(self.api,self.base_path)
         add_busines_route(self.api,self.base_path)
      