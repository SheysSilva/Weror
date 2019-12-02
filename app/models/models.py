from app.db import db
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

class Company(db.Model):
    """
    Create an Company table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Company'

    id = db.Column(db.String(14), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type_random = db.Column(db.String(3), default='000')
    status = db.Column(db.String(10), default='Active', nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Company %d>' % self.id

class NumberDocument(db.Model):
    """docstring for NumberDocument"""
    __tablename__ = 'NumberDocument'

    id = db.Column(db.String(9), primary_key=True)
    status = db.Column(db.String(10), default='Blocked', nullable=False)
    company_id = db.Column(db.String(14), db.ForeignKey('Company.id'), nullable=False)

    def __init__(self, id, company_id):
        self.id = id
        self.company_id = company_id

    def __repr__(self):
        return '<NumberDocument %d>' % self.id

class Keys(db.Model):
    """
    Create an Keys table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Keys'

    id = db.Column(db.String(44), primary_key=True)
    state = db.Column(db.String(2), nullable=False)
    year = db.Column(db.String(2), nullable=False)
    month = db.Column(db.String(2), nullable=False)
    model = db.Column(db.String(2), nullable=False)
    serie = db.Column(db.String(2), nullable=False)
    issue = db.Column(db.String(1), nullable=False)
    status = db.Column(db.String(10), default='Free', nullable=False)
    numberDocument_id = db.Column(db.String(9), db.ForeignKey('NumberDocument.id'), nullable=False)

    def __init__(self, id, state, year, month, model, serie, issue, numberDocument_id):
        self.id = id
        self.state = state
        self.year = year
        self.month = month
        self.model = model
        self.serie = serie
        self.issue = issue
        self.numberDocument_id = numberDocument_id

    def __repr__(self):
        return '<Keys %d>' % self.id
