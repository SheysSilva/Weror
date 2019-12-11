from app.db import db
from flask import jsonify, make_response
from app.util.util import *
from app.models.models import *

def getCompanies():
    companies = Company.query.filter_by(status='Active')
    res = []  
    if companies == None:
        return make_response(jsonify(res), 200)

    for company in companies:
        res.append({
            'id': company.id,
            'name': company.name,
            'status': company.status
        })          
                
    return make_response(jsonify(res), 200)

def getCompanyId(id):
    if isNull(id):
        return make_response(jsonify({'return':'Id is Null!'}), 406)

    company = Company.query.filter_by(id=str(id)).first()

    if not company:
        return make_response(jsonify({'return':'Company not exist!'}), 204)
    res = {
        'id': company.id,
        'name': company.name,
        'status': company.status
    }

    return make_response(jsonify(res), 200)

def postCompany(id, name, random):
    if isNull(id) or isNull(name) or isNull(random):
        return make_response(jsonify({'return':'ID null!'}), 406)

    company = Company.query.filter_by(id=str(id)).first()
        
    if not company:
        company = Company(str(id), str(name), str(random))
        db.session.add(company)
        db.session.commit()
        return make_response(jsonify({'id': company.id, 'name': company.name, 'status': company.status}), 201)
    else:
        return make_response(jsonify({'return': 'Exist Company'}), 200)


def putCompany(id, status, name):
    if isNull(id):
        return make_response(jsonify({'return':'Values is Null'}), 406)

    company = Company.query.filter_by(id=str(id)).first()
        
    if not company:
        return make_response(jsonify({'return': 'Not Exist'}), 204)
    else:
        if isNull(name):
            company.name = str(name)
        if isNull(status):
            company.status = str(status)
        
        db.session.commit()
        company = Company.query.filter_by(id=str(id)).first()
        return make_response(jsonify({'id': company.id, 'name': company.name, 'status': company.status}), 200)

def deleteCompany(id):
    if isNull(id): 
        return deleteCompanies()
    else:
        company = Company.query.filter_by(id=str(id)).first()
            
        if not company:
            return make_response(jsonify({'return': 'Not Exist'}), 204)
        else:
            if company.status == 'Inactive':
                db.session.delete(company)
                db.session.commit()
                return make_response(jsonify({'return':'Success', 'id': company.id, 'name': company.name, 'status': company.status}), 200)
            return make_response(jsonify({'return': 'Company not used', 'id': company.id, 'name': company.name, 'status': company.status}), 200)
        
def deleteCompanies():
    companies = Company.query.filter_by(status='Ok')
    for company in companies:
        db.session.delete(company)
        db.session.commit()
    return make_response(jsonify({'return':'Success'}), 200)

