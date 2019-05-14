from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime
from secrets import token_urlsafe

from app.models import User
from app import db, redis

def verify_token(json):
    json_data = request.get_json()
    email = json_data["email"]
    token_verify = json_data["token"]
    token = redis.hget(email, "field1")
    if(token == token_verify):
        return True
    return False

def data_json():
    json_data = request.get_json(force=True)
    if(not json_data):
        return jsonify({'message': 'No input data provided'}), 400   
    return json_data

class User_CRUD(Resource):

    def get(self):
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        user = User.query.filter_by(email=json_data["email"]).first()
        userdict = {    'id': user.id,
                        'name': user.name,
                        'institution': user.institution,
                        'phone' : user.phone,
                        'born_date' : user.born_date,
                        'sex' : user.sex,
                        'cpf' : user.cpf

        }
        return jsonify(userdict)
        
    def post(self):
        json_data = data_json()
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
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        user = User.query.filter_by(email=json_data["email"]).first()
        aux_data = json_data["born_date"].split("-")
        data = datetime(int(aux_data[0]), int(aux_data[1]), int(aux_data[2]))
        user.name=json_data["name"]
        user.email=json_data["novoemail"]
        user.password=json_data["password"]
        user.institution=json_data["institution"]
        user.phone=json_data["phone"]
        user.born_date=data
        user.sex=json_data["sex"]
        user.cpf=json_data["cpf"]
        db.session.add(user)
        db.session.commit()
        return 200
        
    def delete(self):
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        user = User.query.filter_by(email=json_data["email"]).first()
        db.session.delete(user)
        db.session.commit()
        return 200

class User_Login(Resource):

    def post(self):
        json_data = data_json()
        
        email = json_data["email"]
        password = json_data["password"]
        user = User.query.filter_by(email=email).first()
        if(user.verify_password(password)):
            if(redis.hexists(email, "field1")):
                token = redis.hget(email, "field1")
                return jsonify({"token":token})
            min_expire_token = 25
            number_bytes = 256
            token = token_urlsafe(number_bytes)
            redis.hset(email, "field1", token)
            redis.expire(email, 60*min_expire_token)
            return jsonify({"token":token})
        else:
            return jsonify({"error":"password dont check"}) , 400



