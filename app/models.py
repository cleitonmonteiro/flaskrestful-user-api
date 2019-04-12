from sqlalchemy import Column, Integer, String, Date
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    """
    Create an User table
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String(256))
    institution = Column(String)
    phone = Column(String) # verificar mudanca no formato
    born_date = Column(Date) 
    sex = Column(String(1))
    cpf = Column(String(11), unique=True)
    user_type = Column(Integer)

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