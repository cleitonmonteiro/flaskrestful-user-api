from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime
from secrets import token_urlsafe

from app.models import User
from app import db, redis

class User_CRUD(Resource):
        
    def post(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400
        aux_data = json_data["born_date"].split("-")
        data = datetime(int(aux_data[0]), int(aux_data[1]), int(aux_data[2]))
        new_user = User(
                        name=str(json_data["name"]),
                        email=str(json_data["email"]),
                        password=str(json_data["password"]),
                        institution=str(json_data["institution"]),
                        phone=str(json_data["phone"]),
                        born_date=data,
                        sex=str(json_data["sex"]),
                        cpf=str(json_data["cpf"])
                                    )
        db.session.add(new_user)
        db.session.commit()
        return 200

    def put(self):
        # se estiver correto ele volta e modifica o usuario
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400    
        
        token_verify = json_data["token"]
        user = User.query.filter_by(email=str(email)).first()
        if(user):
            token = redis.hget(user.email)
            # verifica no banco redis 
            if(token == token_verify): # teremos que ver o que realmente pode ser mudado 
                aux_data = json_data["born_date"].split("-")
                data = datetime(int(aux_data[0]), int(aux_data[1]), int(aux_data[2]))
                user.name=json_data["name"]
                user.email=json_data["email"]
                user.password=json_data["password"]
                user.institution=json_data["institution"]
                user.phone=json_data["phone"]
                user.born_date=data
                user.sex=json_data["sex"]
                user.cpf=json_data["cpf"]
                db.session.add(user)
                db.session.commit()
            return 200
        else:
            return jsonify({"error":"este email nao existe"})

    def delete(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400
        token = json_data["token"]
        ###### continua depois...
        


class User_Login(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400
        
        email = json_data["email"]
        password = json_data["password"]
        user = User.query.filter_by(email=email).first()
        if(user.verify_password(password)):
            min_expire_token = 25
            number_bytes = 256
            token = token_urlsafe(number_bytes)
            redis.hset(email, token)
            redis.expire(email, 60*)
            return jsonify{"token":token}
        else:
            return jsonify({"error":"password dont check"}) , 400



