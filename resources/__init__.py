from user import User,User_Login
from flask_restful import Api

def init_resources(app):
    api = Api(app)
    api.add_resource(User,"/user")
    api.add_resource(User_Login, "/user/<email>")
    return app

