from flask_restful import Resource
from flask.json import jsonify
from flask import request

from app.models import User
from app import db

class User_Resource(Resource):
    def get(self, email):
        user = User.query.filter_by(email = email).first()
        return jsonify(user)

    def post(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400
        new_user_id=0
        if(User.query.all()):
            new_user_id = User.query.all()[-1] + 1
        new_user = User(id=int(new_user_id),
                        name=str(json_data["name"]),
                        email=str(json_data["email"]),
                        password=str(json_data["password"]),
                        institution=str(json_data["institution"]),
                        phone=str(json_data["phone"]),
                        born_date=str(json_data["born_date"]),
                        sex=str(json_data["sex"]),
                        cpf=str(json_data["cpf"]),
                        user_type=int(json_data["user_type"])
                                    )
        db.session.add(new_user)
        db.session.commit()
        return 200