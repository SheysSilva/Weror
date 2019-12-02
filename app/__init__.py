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
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.models.models import Keys, Company, NumberDocument

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

    #### KEYS ####
    @app.route(keys, methods=['GET'])
    def getKeys():
        return key.getKeys()

    @app.route(keys+'<id>', methods=['GET'])
    def getKeyId(id):
        return key.getKeyId(id)

    @app.route(keys, methods=['POST'])
    def postKey():
        id = request.form.get('id')
        state = request.form.get('state')
        year = request.form.get('year')
        month = request.form.get('month')
        model = request.form.get('model')
        serie = request.form.get('serie')
        issue = request.form.get('issue')
        numberDocumentId = request.form.get('numberDocumentId')

        return key.postKey(id, state, year, month, model, serie, issue, numberDocumentId)

    @app.route(keys, methods=['PUT'])
    def putKey():
        id = request.form.get('id')
        status = request.form.get('status')

        return key.putKey(id, status)
    
    @app.route(keys, methods=['DELETE'])
    def deleteKey():
        id = request.form.get('id')
        return key.deleteKey(id)
        
    def deleteKeys():
        return key.deleteKeys()

    ### COMPANIES ###

    @app.route(companies, methods=['GET'])
    def getCompanies():
        return company.getCompanies()

    @app.route(companies+'<id>', methods=['GET'])
    def getCompanyId(id):
        return company.getCompanyId(id)

    @app.route(companies, methods=['POST'])
    def postCompany():
        id = request.form.get('id')
        name = request.form.get('name')

        return company.postCompany(id, name)

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

    @app.route(numberDocuments, methods=['GET'])
    def getNumberDocuments():
        return numberDocument.getNumberDocuments()

    @app.route(numberDocuments+'<id>', methods=['GET'])
    def getNumberDocumentId(id):
        return numberDocument.getNumberDocumentId(id)

    @app.route(numberDocuments, methods=['POST'])
    def postNumberDocument():
        id = request.form.get('id')
        id_company = request.form.get('id_company')

        return numberDocument.postNumberDocument(id, id_company)

    @app.route(numberDocuments, methods=['PUT'])
    def putNumberDocument():
        id = request.form.get('id')
        status = request.form.get('status')

        return numberDocument.putNumberDocument(id, status)

    @app.route(numberDocuments, methods=['DELETE'])
    def deleteNumberDocument():
        id = request.form.get('id')
        return numberDocument.deleteNumberDocument(id)

    @app.route(relationships, methods=['GET'])
    def getRelationship():
        id_company = request.form.get('id_company')
        id_numberDocument = request.form.get('id_numberDocument')
        return relationship.getRelationship(id_company, id_numberDocument)

    @app.route(relationships, methods=['POST'])
    def postRelationship():
        id_company = request.form.get('id_company')
        id_numberDocument = request.form.get('id_numberDocument')

        return relationship.postRelationship(id_company, id_numberDocument)

    @app.route(relationships, methods=['PUT'])
    def putRelationship():
        id_company = request.form.get('id_company')
        id_numberDocument = request.form.get('id_numberDocument')
        status = request.form.get('status')

        return relationship.putRelationship(id_company, id_numberDocument, status)

    @app.route(relationships, methods=['DELETE'])
    def deleteRelationship():
        id_company = request.form.get('id_company')
        id_numberDocument = request.form.get('id_numberDocument')

        return relationship.deleteRelationship(id_company, id_numberDocument)

    return app