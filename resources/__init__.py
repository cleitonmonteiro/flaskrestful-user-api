from user import User_CRUD,User_Login,User_Information
from flask_restful import Api

def init_resources(app):
    api = Api(app)
    api.add_resource(User_CRUD,"/user")
    api.add_resource(User_Information,"/userinfo")
    api.add_resource(User_Login, "/user/login")
    return app

