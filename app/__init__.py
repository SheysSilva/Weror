from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import *
from flask_migrate import Migrate
from app.models import key, company, numberDocument, relationship
from app.db import db
from app.routes import *

from config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    migrate = Migrate(app, db)

    db.init_app(app)

    from app.models.models import Company, NumberDocument, Keys

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/set/', methods=['GET'])
    def setStatus():
        keys = Keys.query.filter_by(status='Using')
        res = []
        for key in keys:
            key.status = 'Free'
            db.session.commit()

            res.append(
                {
                    'id': key.id, 
                    'status': key.status
                }
            )              
                
        return make_response(jsonify(res), 200)

    @app.route('/using/', methods=['GET'])
    def getStatusUsing():
        keys = Keys.query.filter_by(status='Using')
        res = []
        for key in keys:
            res.append(
                {
                    'id': key.id, 
                    'status': key.status
                }
            )              
                
        return make_response(jsonify(res), 200)

    @app.route('/free/', methods=['GET'])
    def getStatusFree():
        keys = Keys.query.filter_by(status='Free')
        res = []
        for key in keys:
            res.append(
                {
                    'id': key.id, 
                    'status': key.status
                }
            )          
                
        return make_response(jsonify(res), 200)

    @app.route('/ok/', methods=['GET'])
    def getStatusOK():
        keys = Keys.query.filter_by(status='Ok')
        res = []
        for key in keys:
            res.append(
                {
                    'id': key.id, 
                    'status': key.status
                }
            )               
                
        return make_response(jsonify(res), 200)

    ### COMPANIES ###

    @app.route(companies, methods=['GET'])
    def getCompanies():
        return company.getCompanies()

    @app.route(companies+'/<id>', methods=['GET'])
    def getCompanyId(id):
        return company.getCompanyId(id)

    @app.route(companies, methods=['POST'])
    def postCompany():
        id = request.form.get('id')
        name = request.form.get('name')
        random = request.form.get('random')

        return company.postCompany(id, name, random)

    @app.route(companies, methods=['PUT'])
    def putCompany():
        id = request.form.get('id')
        status = request.form.get('status')
        return company.putCompany(id, status)

    @app.route(companies, methods=['DELETE'])
    def deleteCompany():
        id = request.form.get('id')
        return company.deleteCompany(id)

    ### Number Document ###

    @app.route(companies+'/<string:id_company>'+numberDocuments, methods=['GET'])
    def getNumberDocuments(id_company):
        return numberDocument.getNumberDocumentCompanyId(id_company)

    @app.route(companies+'/<string:id_company>'+numberDocuments+'/<id>', methods=['GET'])
    def getNumberDocumentId(id, id_company):
        return numberDocument.getNumberDocumentId(id)

    @app.route(companies+'/<string:id_company>'+numberDocuments, methods=['POST'])
    def postNumberDocument(id_company):
        id = request.form.get('id')
        id_company = str(id_company)

        return numberDocument.postNumberDocument(id, id_company)

    @app.route(companies+'/<string:id_company>'+numberDocuments, methods=['PUT'])
    def putNumberDocument(id_company):
        id = request.form.get('id')
        status = request.form.get('status')

        return numberDocument.putNumberDocument(id, status)

    @app.route(companies+'/<string:id_company>'+numberDocuments, methods=['DELETE'])
    def deleteNumberDocument(id_company):
        id = request.form.get('id')
        return numberDocument.deleteNumberDocument(id)

    #### KEYS ####
    @app.route(companies+'/<string:id_company>'+keys, methods=['GET'])
    def getKeys(id_company):
        return key.getKeys(id_company)

    @app.route(companies+'/<string:id_company>'+numberDocuments+keys+'/<string:id>', methods=['GET'])
    def getKeyId(id):
        return key.getKeyId(id)

    @app.route(companies+'/<string:id_company>'+numberDocuments+'/<string:id_number>'+keys, methods=['POST'])
    def postKey(id_company, id_number):
        id = request.form.get('id')
        state = request.form.get('state')
        year = request.form.get('year')
        month = request.form.get('month')
        model = request.form.get('model')
        serie = request.form.get('serie')
        issue = request.form.get('issue')
        numberDocumentId = str(id_number)

        return key.postKey(id, state, year, month, model, serie, issue, numberDocumentId)

    @app.route(companies+'/<string:id_company>'+numberDocuments+keys+'/<string:id>', methods=['PUT'])
    def putKey(id_company):
        id = request.form.get('id')
        status = request.form.get('status')

        return key.putKey(id, status)
    
    @app.route(companies+'/<string:id_company>'+numberDocuments+keys, methods=['DELETE'])
    def deleteKey():
        id = request.form.get('id')
        return key.deleteKey(id)
        
    def deleteKeys():
        return key.deleteKeys()

    return app