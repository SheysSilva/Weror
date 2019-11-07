from app import db

class Chaves(db.Model):
    """
    Create an Chaves table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Chaves'

    id = db.Column(db.String(44), primary_key=True)
    status = db.Column(db.String(10), default='Free')

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
    status = db.Column(db.String(10), default='Active')


    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<Company %d>' % self.id

class NumberDocument(db.Model):
    """docstring for NumberDocument"""
    __tablename__ = 'NumberDocument'

    id = db.Column(db.String(9), primary_key=True)
    month = db.Column(db.String(20), primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    cnpj = db.Column(db.String(14), db.ForeignKey('Company.id'),
        nullable=False)

    def __init__(self, id, month, status, cnpj):
        self.id = id,
        self.month = month,
        self.status = status,
        self.cnpj = cnpj
    
    def __repr__(self):
        return '<NumberDocument %d>' % self.id