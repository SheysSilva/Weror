from app.db import db
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

class Chaves(db.Model):
    """
    Create an Chaves table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Chaves'

    id = db.Column(db.String(44), primary_key=True)
    status = db.Column(db.String(10), default='Free', nullable=False)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<Chaves %d>' % self.id

class Company(db.Model):
    """
    Create an Company table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Company'

    id = db.Column(db.String(14), primary_key=True)
    status = db.Column(db.String(10), default='Active', nullable=False)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<Company %d>' % self.id

class NumberDocument(db.Model):
    """docstring for NumberDocument"""
    __tablename__ = 'NumberDocument'

    id = db.Column(db.String(9), primary_key=True)
    month = db.Column(db.String(2), primary_key=True)
    year = db.Column(db.String(2), primary_key=True)
    status = db.Column(db.String(10), default='Blocked', nullable=False)
    relationship = db.relationship('Relationship', backref='NumberDocument')

    def __init__(self, id, month, year, id_company):
        self.id = id,
        self.month = month
        self.year = year

    def __repr__(self):
        return '<NumberDocument %d>' % self.id

class Relationship(db.Model):
    """docstring for Relationship"""
    __tablename__ = 'Relationship'

    id_company = db.Column(db.String(14), db.ForeignKey('Company.id'), primary_key=True, nullable=False)
    id_numberDocument = db.Column(db.String(9), db.ForeignKey('NumberDocument.id'), primary_key=True, nullable=False)
    status = db.Column(db.String(10), default='Active',  nullable=False)

    def __init__(self, id_company, id_numberDocument):
        self.id_company = id_company,
        self.id_numberDocument = id_numberDocument