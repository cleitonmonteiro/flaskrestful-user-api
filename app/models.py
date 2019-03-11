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

class Event(db.Model):
    """
    Create an Event table
    """

    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    area = Column(String)
    init_date = Column(Date) 
    end_date = Column(Date) 
    description = Column(String) # limitar tamanho???
    contact_email = Column(String)

    def __repr__(self):
        return '<Event: {}>'.format(self.name)

class Trail(db.Model):
    """
    Create an Trail table
    """

    __tablename__ = 'trails'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer) # add foreign key
    reponsible_id = Column(Integer) #add foreign key
    name = Column(String)
    trail_description = Column(String)
    subarea = Column(String)
    init_date_submission = Column(Date) 
    end_date_submission = Column(Date) 
    number_measurer = Column(Integer)
    #forma_submission(?) <<  tipo?
    #criterion_de_avaliacao << ???
    
    def __repr__(self):
        return '<Trail: {}>'.format(self.name)

class Submission(db.Model):
    """
    Create an Submission table
    """

    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True)
    #id_autor << foreign key, pode referenciar um ou varios users, irei fazer apos colocar as fk
    title = Column(String) # unique?
    description = Column(String)
    #arquivo << qual o tipo, ou nao e nescessario? pdf??
    state = Column(String)
    note = Column(Integer)

    def __repr__(self):
        return '<Submission: {}>'.format(self.title)

class Criterion(db.Model):
    """
    Create an Criterion table
    """
    
    __tablename__= 'criterions'

    id = Column(Integer, primary_key=True)
    #id_trail << add foreign key
    description = Column(String)
    weight = Column(Integer) #vai ser um valor ou uma porcentagem da nota total?

    def __repr__(self):
        return '<Criterion: {}>'.format(self.descricao_criterion)

