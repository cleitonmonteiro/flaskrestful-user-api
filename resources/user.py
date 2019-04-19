from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from app.models import User
from app import db

class User_Register(Resource):
    def get(self):
        return jsonify({"mensagem teste":"servidor funcionando"})
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
        # verifica no banco redis 
        # se estiver correto ele volta e modifica o usuario
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400    
        if(True):
            user = User.query.filter_by(email=str(email)).first()
        else:
            return jsonify({"error":"este token espirou"})


class User_Login(Resource):
    
    def get(self, email):
        user = User.query.filter_by(email=str(email)).first()
        
        user_taked={}
        user_taked["name"]=user.name
        user_taked["email"]=user.email
        user_taked["password_hash"]=user.password

        return jsonify(user_taked)