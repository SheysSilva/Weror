from app.db import db
from flask import jsonify, make_response
from app.util.util import *
from app.models.models import *
from app.models import relationship


def getNumberDocuments():
    numberDocuments = NumberDocument.query.all()
    res = []
    
    for numberDocument in numberDocuments:

        res.append({
            'id': numberDocument.id,
            'status': numberDocument.status,
            'company_id': numberDocument.company_id
        })       
                
    return make_response(jsonify(res), 200)

def getNumberDocumentId(id):
    if isNull(id):
        return make_response(jsonify({'return':'Id is Null!'}), 406)

    numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
        
    if not numberDocument:
        return make_response(jsonify({'return':'Number Document not exist!'}), 204)
    res = {
        'id': numberDocument.id,
        'status': numberDocument.status,
        'company_id': numberDocument.company_id
    }

    return make_response(jsonify(res), 200)

def getNumberDocumentCompanyId(id):
    if isNull(id):
        return make_response(jsonify({'return':'Id is Null!'}), 406)

    numberDocument = NumberDocument.query.filter_by(company_id=str(id)).first()
        
    if not numberDocument:
        return make_response(jsonify({'return':'Number Document not exist!'}), 204)
    res = {
        'id': numberDocument.id,
        'status': numberDocument.status,
        'company_id': numberDocument.company_id
    }

    return make_response(jsonify(res), 200)

def postNumberDocument(id, id_company):

    if isNull(id) or isNull(id_company):
        return make_response(jsonify({'return':'Values Null!'}), 406)
    
    numberDocument = NumberDocument.query.filter_by(id=str(id)).first()

    if not numberDocument:
        isCnpj = Company.query.filter_by(id=str(id_company)).first()

        if not isCnpj:
            return make_response(jsonify({'return': 'Company not exist'}), 204)


        numberDocument = NumberDocument(str(id), str(id_company))
        db.session.add(numberDocument)
        db.session.commit()

        res = {
            'id': numberDocument.id,
            'status': numberDocument.status, 
            'company_id': numberDocument.company_id
        }
        return make_response(jsonify(res), 201)

    return make_response(jsonify({'return': 'Exist NumberDocument'}), 200)


def putNumberDocument(id, status):
    if isNull(id):
        return make_response(jsonify({'return':'Id is Null!'}), 406)
    
    numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
        
    if not numberDocument:
        return make_response(jsonify({'return': 'Not Exist'}), 204)
    else:
        if not isNull(status):
            numberDocument.status = status
            
        db.session.commit()
        numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
            
        res = {
            'id': numberDocument.id,
            'status': numberDocument.status,
            'company_id': numberDocument.company_id
        }
        return make_response(jsonify(res), 200)

def deleteNumberDocument(id):
    if isNull(id): 
        return make_response(jsonify({'return':'Ids Null!'}), 406)
    else:
        numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
            
        if not numberDocument:
            return make_response(jsonify({'return': 'Not Exist'}), 204)
        else:
            if numberDocument.status == 'Inactive':
                db.session.delete(numberDocument)
                db.session.commit()

                return make_response(jsonify({
                    'return':'Success', 
                    'id': numberDocument.id,
                    'status': numberDocument.status,
                    'company_id': numberDocument.company_id
                }), 200)

            return make_response(jsonify({
                'return': 'Number Document is used', 
                'id': numberDocument.id,
                'status': numberDocument.status,
                'company_id': numberDocument.company_id
            }), 200)
