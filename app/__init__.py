from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import key
from app.models import company
from app.models import relationship
from app.db import db

from config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    keys= '/keys/'
    companies= '/companies/'
    numberDocument = '/numberDocument/'

    from app.models.models import Chaves, Company, NumberDocument

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/set/', methods=['GET'])
    def setStatus():
        chaves = Chaves.query.filter_by(status='Using')
        res = {}
        for chave in chaves:
            chave.status = 'Free'
            db.session.commit()

            res[chave.id] = {
                'id': chave.id,
                'status': chave.status
            }          
                
        return jsonify(res)

    @app.route('/using/', methods=['GET'])
    def getStatusUsing():
        chaves = Chaves.query.filter_by(status='Using')
        res = {}
        for chave in chaves:
            res[chave.id] = {
                'id': chave.id,
                'status': chave.status
            }          
                
        return jsonify(res)

    @app.route('/free/', methods=['GET'])
    def getStatusFree():
        chaves = Chaves.query.filter_by(status='Free')
        res = {}
        for chave in chaves:
            res[chave.id] = {
                'id': chave.id,
                'status': chave.status
            }          
                
        return jsonify(res)

    @app.route('/ok/', methods=['GET'])
    def getStatusOK():
        chaves = Chaves.query.filter_by(status='Ok')
        res = {}
        for chave in chaves:
            res[chave.id] = {
                'id': chave.id,
                'status': chave.status
            }          
                
        return jsonify(res)

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
        return key.postKey(id)

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
        return company.postCompany(id)

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

    @app.route(numberDocument, methods=['GET'])
    def getNumberDocuments():
        numberDocuments = NumberDocument.query.all()
        res = {}
        
        for numberDocument in numberDocuments:

            res[numberDocument.id] = {
                'id': numberDocument.id,
                'month': numberDocument.month,
                'status': numberDocument.status,
                'cnpj': numberDocument.cnpj
            }          
                
        return jsonify(res)

    @app.route(numberDocument+'<id>', methods=['GET'])
    def getNumberDocumentId(id):
        if isNull(id):
            return jsonify({'return':'Id is Null!'})

        numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
        
        if not numberDocument:
            return jsonify({'return':'Number Document not exist!'})
        res = {
            'id': numberDocument.id,
            'month': numberDocument.month,
            'status': numberDocument.status,
            'cnpj': numberDocument.cnpj
        }

        return jsonify(res)

    @app.route(numberDocument, methods=['POST'])
    def postNumberDocument():
        id = request.form.get('id')
        month = request.form.get('month')
        status = request.form.get('status')
        cnpj = request.form.get('cnpj')

        if isNull(id) or isNull(month) or isNull(status) or isNull(cnpj):
            return jsonify({'return':'Values Null!'})
        else:
            isCnpj = Company.query.filter_by(id=str(cnpj)).first()

            if not isCnpj:
                company = Company(str(cnpj))
                db.session.add(company)
                db.session.commit()

            numberDocument = NumberDocument(str(id), str(month), str(status), str(cnpj))
            db.session.add(numberDocument)
            db.session.commit()
            res = {
                'id': numberDocument.id,
                'month': numberDocument.month,
                'status': numberDocument.status,
                'cnpj': numberDocument.cnpj
            }
            return jsonify(res)

    @app.route(numberDocument, methods=['PUT'])
    def putNumberDocument():
        id = request.form.get('id')
        month = request.form.get('month')
        status = request.form.get('status')
        cnpj = request.form.get('cnpj')

        if isNull(id):
            return jsonify({'return':'Id is Null!'})

        numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
        
        if not numberDocument:
            return jsonify({'return': 'Not Exist'})
        else:
            if not isNull(month):
                numberDocument.month = month
            if not isNull(status):
                numberDocument.status = status
            if not isNull(cnpj):
                numberDocument.cnpj = cnpj
                
            db.session.commit()
            numberDocument = Company.query.filter_by(id=str(id)).first()
            
            res = {
                'id': numberDocument.id,
                'month': numberDocument.month,
                'status': numberDocument.status,
                'cnpj': numberDocument.cnpj
            }
            return jsonify(res)

    @app.route(numberDocument, methods=['DELETE'])
    def deleteNumberDocument():
        id = request.form.get('id')

        if isNull(id): 
            return jsonify({'return':'Ids Null!'})
        else:
            numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
            
            if not numberDocument:
                return jsonify({'return': 'Not Exist'})
            else:
                if numberDocument.status == 'Inactive':
                    db.session.delete(numberDocument)
                    db.session.commit()

                    return jsonify({
                        'return':'Success', 
                        'id': numberDocument.id, 
                        'month': numberDocument.month,
                        'status': numberDocument.status,
                        'cnpj': numberDocument.cnpj
                    })

                return jsonify({
                    'return': 'Number Document is used', 
                    'id': numberDocument.id,
                    'month': numberDocument.month,
                    'status': numberDocument.status,
                    'cnpj': numberDocument.cnpj
                })

    def isNull(a):
        a = str(a)
        if not a or not a.strip() or a == 'None':
            return True
        return False

    
    return app