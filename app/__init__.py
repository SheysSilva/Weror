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

	# temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/chaves/', methods=['GET'])
    def getAll():
        chaves = Chaves.query.filter_by(verify=False).limit(64)
        res = {}
        for chave in chaves:
            res[chave.id] = {
                'id': chave.id,
                'verify': chave.verify
            }
        return jsonify(res)

    @app.route('/chaves/<id>', methods=['GET'])
    def getId(id):
        chave = Chaves.query.filter_by(id=str(id)).first()
        if not chave:
            abort(404)
        res = {
            'id': chave.id,
            'verify': chave.verify
        }

        return jsonify(res)

    @app.route('/chaves/', methods=['POST'])
    def post():
        id = request.form.get('id')
        if not id:
            return 'ID null!'
        else:
        	chave = Chaves(str(id))
        	db.session.add(chave)
        	db.session.commit()
        	return jsonify({'id': chave.id})

    @app.route('/chaves/', methods=['PUT'])
    def put():
        id = request.form.get('id')
        chave = Chaves.query.filter_by(id=id).first()
        
        if not chave:
            return jsonify({'return': 'Not Exist'})
        else:
            chave.verify = True
            db.session.commit()
            chave = Chaves.query.filter_by(id=id).first()
            return jsonify({'id': chave.id, 'verify': chave.verify})
    
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
                if chave.verify:
                    db.session.delete(chave)
                    db.session.commit()
                    return jsonify({'return':'Success', 'id': chave.id, 'verify': chave.verify})
                return jsonify({'return': 'Key not used', 'id': chave.id, 'verify': chave.verify})
        
    def deleteAll():
        chaves = Chaves.query.filter_by(verify=True)
        for chave in chaves:
            db.session.delete(chave)
            db.session.commit()
        return jsonify({'return':'Success'})

    return app