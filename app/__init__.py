from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import *
from flask_migrate import Migrate
from app.models import key, company, month
from app.util.generateKey import generate
from app.db import db
from app.routes import *
import json
from config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    migrate = Migrate(app, db)

    db.init_app(app)

    from app.models.models import Company, Keys, Month

    def createKeys():
        companiess = company.getCompanies()
        companiess = companiess.json()

        for c in companiess:
            cnpj = c['id']
            month = month.getMonthCompanyId(id_company)

            if not month:
                print("SEM RETORNO")
            else:
                month=month.json()
                month=month[0]
                inicial=month['inicial']
                for number in range(inicial, inicial+1000):
                    id = generate(month['state'], month['year'], month['id'], cnpj, month['model'], month['serie'], number, month['issue'])
                    key.postKey(id, month['state'], str(month['year'])[2:4], month['id'], month['model'], month['serie'], month['issue'], number, cnpj)
    

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

    #### KEYS ####
    @app.route(keys, methods=['GET'])
    def getKeys():
        return key.getKeysFree()

    @app.route(companies+'/<string:id_company>'+keys, methods=['GET'])
    def getKeysCompanyIdi(id_company):
        return key.getKeys(id_company)

    @app.route(companies+'/<string:id_company>'+keys+'/<string:id>', methods=['GET'])
    def getKeyId(id):
        return key.getKeyId(id)

    @app.route(companies+'/<string:id_company>'+keys, methods=['POST'])
    def postKey(id_company):
        id = request.form.get('id')
        state = request.form.get('state')
        year = request.form.get('year')
        month = request.form.get('month')
        model = request.form.get('model')
        serie = request.form.get('serie')
        issue = request.form.get('issue')
        id_company = str(id_company)

        return key.postKey(id, state, year, month, model, serie, issue, id_company)

    @app.route(companies+'/<string:id_company>'+keys+'/<string:id>', methods=['PUT'])
    def putKey(id_company, id):
        id = str(id)
        status = request.form.get('status')

        return key.putKey(id, status)
    
    @app.route(companies+'/<string:id_company>'+keys, methods=['DELETE'])
    def deleteKey():
        id = request.form.get('id')
        return key.deleteKey(id)
        
    def deleteKeys():
        return key.deleteKeys()

    #### Month ####
    @app.route(months, methods=['GET'])
    def getMonths():
        return month.getMonths()

    @app.route(months+'/<string:id_month>', methods=['GET'])
    def getMonth(id_month):
        return month.getMonth(id_month)

    @app.route(companies+'/<string:id_company>'+months, methods=['GET'])
    def getMonthsCompany(id_company):
        return month.getMonthCompanyId(id_company)

    @app.route(companies+'/<string:id_company>'+months+'/<string:id_month>', methods=['GET'])
    def getMonthIdCompany(id_company, id_month):
        return month.getMonthId(id_month, id_company)

    @app.route(companies+'/<string:id_company>'+months, methods=['POST'])
    def postMonthId(id_company):
        id = request.form.get('id')
        year = request.form.get('year')
        model = request.form.get('model')
        serie = request.form.get('serie')
        issue = request.form.get('issue')
        state = request.form.get('state')
        inicial = request.form.get('inicial')
        id_company = str(id_company)
        
        return month.postMonth(id, year, serie, model, issue, state, inicial, id_company)

    return app