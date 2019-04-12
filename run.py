import os

from flask_restful import Api
from app import create_app
from resources.user import User_Resource 

app = create_app(os.getenv('FLASK_CONFIG') or "default")
api = Api(app)

api.add_resource(User_Resource,"/user")

if __name__ == "__main__":
    app.run()