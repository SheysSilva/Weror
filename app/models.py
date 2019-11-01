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

