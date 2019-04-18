import os
#from flask_restful import Api

from app import create_app
from resources import init_resources

#app = create_app(os.getenv('FLASK_CONFIG') or "default")
app = create_app("development")
app = init_resources(app) # talvez essa funcao nao precise retornar nada 
#api = Api(app)


if __name__ == "__main__":
    app.run()