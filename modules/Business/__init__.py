from .controller import CreateBusiness,User_Busines_Mapper,Business_login

def routes(api,base_path):
    pth = base_path + '/business'
    api.add_resource(CreateBusiness,pth + '/add')
    api.add_resource(User_Busines_Mapper,pth + '/addmap')
    api.add_resource(Business_login,pth + '/login')
    