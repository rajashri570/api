from db_config.database import db
from .businesDAO import Business,LinkUserBusiness
from flask_jwt_extended import create_access_token



class BusinessFun(Business):
    def __init__(self):
        pass
    
    def save(self,body):
        try:
            print(body)
            new_business = Business(**body)
            db.session.add(new_business)
            db.session.commit()
            return "Bisuness added successfully!!!"
        except Exception as e:
            print(f"dddddd {e}")
            return "error"
   
class MappingFun(LinkUserBusiness):
    def __init__(self):
        pass
    def save(self,body):
        try:
            print(body)
            new_link = LinkUserBusiness(**body)
            db.session.add(new_link)
            db.session.commit()
            return "linking added successfully!!!"
        except Exception as e:
            print(f"dddddd {e}")
            return "might u given invalid uid or bid!!"
        
    def login(self,id,header):
        try:
            
            rec = LinkUserBusiness.query.filter_by(uid=id).first()
            header['bid'] = rec.bid
            access_token = create_access_token(identity=id, additional_claims=header)
            
            # token = create_access_token(identity=userid,additional_claims=headers)
            print(access_token)
            return access_token
        
        except:
            return "Error in creating business acces token!!!"
  
    # def login(self,body):
        # try:
            
        #     print("login function in buiness.py!!!")
        #     uid = body.get('uid')
        #     bid = body.get('bid')
        #     print("login data : ",uid,bid)
        #     rec = LinkUserBusiness.query.filter_by(uid=uid).first()
        #     if rec and rec.bid == bid:
        #         role = rec.role
        #         # return "role:"+role
        #         access_token = create_access_token(identity=rec.id)
        #         # additional_claims = {"roles": user.role, "name": user.first_name}
        #         access_token = create_access_token(identity=uid, additional_claims={"roles": role})
        #         # print(user.role)
        #         return f"access_token': {access_token}", 200
        #     # return "successfully looged in!!!"
        # except Exception as e:
        #     return "error in login"
            # if user and rec.bid 
    
    # def checkBusiness(self,body):
        # try:
        #     print("in check business function!!!")
        #     uid = body.get('current_user')
        #     rec = LinkUserBusiness.query.filter_by(uid=uid).first()
        #     if rec :
        #         return "user have business!!!"
        #     else:
        #         return "No business with this user"
        # except Exception as e:
        #     return "Error in checking the business...!"            
            

            
        