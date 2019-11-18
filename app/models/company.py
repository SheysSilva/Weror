from app.db import db
from app.util.util import *
from app.models.models import *

def getCompanies():
    companies = Company.query.filter_by(status='Active')
    res = {}
        
    for company in companies:

        res[company.id] = {
            'id': company.id,
            'status': company.status
        }          
                
    return jsonify(res)

def getCompanyId(id):
    if isNull(id):
        return jsonify({'return':'Id is Null!'})

    company = Company.query.filter_by(id=str(id)).first()

    if not company:
        return jsonify({'return':'Company not exist!'})
    res = {
        'id': company.id,
        'status': company.status
    }

    return jsonify(res)

def postCompany(id):
    if isNull(id):
        return jsonify({'return':'ID null!'})
    else:
        company = Company(str(id))
        db.session.add(company)
        db.session.commit()
        return jsonify({'id': company.id, 'status': company.status})

def putCompany(id, status):
    if isNull(id) or isNull(status):
        return jsonify({'return':'Values is Null'})

    company = Company.query.filter_by(id=str(id)).first()
        
    if not company:
        return jsonify({'return': 'Not Exist'})
    else:
        company.status = str(status)
        db.session.commit()
        company = Company.query.filter_by(id=str(id)).first()
        return jsonify({'id': company.id, 'status': company.status})

def deleteCompany(id):
    if isNull(id): 
        return deleteCompanies()
    else:
        company = Company.query.filter_by(id=str(id)).first()
            
        if not company:
            return jsonify({'return': 'Not Exist'})
        else:
            if company.status == 'Inactive':
                db.session.delete(company)
                db.session.commit()
                return jsonify({'return':'Success', 'id': company.id, 'status': company.status})
            return jsonify({'return': 'Key not used', 'id': company.id, 'status': company.status})
        
def deleteCompanies():
    companies = Company.query.filter_by(status='Ok')
    for company in companies:
        db.session.delete(company)
        db.session.commit()
    return jsonify({'return':'Success'})

