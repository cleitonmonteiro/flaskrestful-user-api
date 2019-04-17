import os

from flask_restful import Api
from app import create_app
from resources.user import User, User_Login

app = create_app(os.getenv('FLASK_CONFIG') or "default")
api = Api(app)

api.add_resource(User,"/user")
api.add_resource(User_Login, "/user/<email>")



if __name__ == "__main__":
    app.run()