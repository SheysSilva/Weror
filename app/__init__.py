from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.models import Chaves

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/chaves/', methods=['GET'])
    def getAll():
        chaves = Chaves.query.filter_by(status='Free').limit(64)
        res = {}
        for chave in chaves:
            chave.status = 'Using'
            db.session.commit()

            res[chave.id] = {
                'id': chave.id,
                'status': chave.status
            }          
                
        return jsonify(res)

    @app.route('/chaves/<id>', methods=['GET'])
    def getId(id):
        chave = Chaves.query.filter_by(id=str(id)).first()
        if not chave:
            abort(404)
        res = {
            'id': chave.id,
            'status': chave.status
        }

        return jsonify(res)

    @app.route('/chaves/', methods=['POST'])
    def post():
        id = request.form.get('id')
        if not id:
            return jsonify({'return':'ID null!'})
        else:
        	chave = Chaves(str(id))
        	db.session.add(chave)
        	db.session.commit()
        	return jsonify({'id': chave.id})

    @app.route('/chaves/', methods=['PUT'])
    def put():
        id = request.form.get('id')
        status = request.form.get('status')
        status = str(status)
        chave = Chaves.query.filter_by(id=id).first()
        
        if not chave:
            return jsonify({'return': 'Not Exist'})
        if not status or not status.strip() or status == 'None':
            return jsonify({'return':'Status is Null'})
        else:
            chave.status = status
            db.session.commit()
            chave = Chaves.query.filter_by(id=id).first()
            return jsonify({'id': chave.id, 'status': chave.status})
    
    @app.route('/chaves/', methods=['DELETE'])
    def delete():
        id = request.form.get('id')
        if not id: 
            return deleteAll()
        else:
            chave = Chaves.query.filter_by(id=id).first()
            
            if not chave:
                return jsonify({'return': 'Not Exist'})
            else:
                if chave.status == 'Ok':
                    db.session.delete(chave)
                    db.session.commit()
                    return jsonify({'return':'Success', 'id': chave.id, 'status': chave.status})
                return jsonify({'return': 'Key not used', 'id': chave.id, 'status': chave.status})
        
    def deleteAll():
        chaves = Chaves.query.filter_by(status='Ok')
        for chave in chaves:
            db.session.delete(chave)
            db.session.commit()
        return jsonify({'return':'Success'})

    return app