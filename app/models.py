#from sqlalchemy import Column, Integer, String, Date
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

from app import db


class User(db.Model):
    """
    Create an User table
    """

    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String(256))
    institution = db.Column(db.String)
    phone = db.Column(db.String) # verificar mudanca no formato
    born_date = db.Column(db.Date) 
    sex = db.Column(db.String(1))
    cpf = db.Column(db.String(11), unique=True)
    #user_type = Column(Integer)

    @property
    def password(self):
        raise AttributeError("A senha não á um atributo que pode ser lido.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.name)