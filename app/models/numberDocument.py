from app.db import db
from flask import jsonify
from app.util.util import *
from app.models.models import *
from app.models import relationship


def getNumberDocuments():
    numberDocuments = NumberDocument.query.all()
    res = {}
    
    for numberDocument in numberDocuments:

        res[numberDocument.id] = {
            'id': numberDocument.id,
            'month': numberDocument.month,
            'year': numberDocument.year,
            'status': numberDocument.status
        }          
                
    return jsonify(res)

def getNumberDocumentId(id):
    if isNull(id):
        return jsonify({'return':'Id is Null!'})

    numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
        
    if not numberDocument:
        return jsonify({'return':'Number Document not exist!'})
    res = {
        'id': numberDocument.id,
        'month': numberDocument.month,
        'year': numberDocument.year,
        'status': numberDocument.status
    }

    return jsonify(res)

def postNumberDocument(id, month, year, id_company):

    if isNull(id) or isNull(month) or isNull(year) or isNull(id_company):
        return jsonify({'return':'Values Null!'})
    
    numberDocument = NumberDocument.query.filter_by(id=str(id)).first()

    if not numberDocument:
        isCnpj = Company.query.filter_by(id=str(id_company)).first()

        if not isCnpj:
            company = Company(str(id_company))
            db.session.add(company)
            db.session.commit()

        numberDocument = NumberDocument(str(id), str(month), str(year))
        db.session.add(numberDocument)
        db.session.commit()

        relationship.postRelationship(str(id_company), str(id))

        res = {
            'id': numberDocument.id,
            'month': numberDocument.month,
            'year': numberDocument.year,
            'status': numberDocument.status
        }
        return jsonify(res)

    return jsonify({'return': 'Exist NumberDocument'})


def putNumberDocument(id, month, year, status):
    if isNull(id):
        return jsonify({'return':'Id is Null!'})
    
    numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
        
    if not numberDocument:
        return jsonify({'return': 'Not Exist'})
    else:
        if not isNull(month):
            numberDocument.month = month
        if not isNull(year):
            numberDocument.year = year
        if not isNull(status):
            numberDocument.status = status
            
        db.session.commit()
        numberDocument = NumberDocument.query.filter_by(id=str(id)).first()
            
        res = {
            'id': numberDocument.id,
            'month': numberDocument.month,
            'year': numberDocument.year,
            'status': numberDocument.status
        }
        return jsonify(res)

def deleteNumberDocument(id):
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
                    'year': numberDocument.year,
                    'status': numberDocument.status
                })

            return jsonify({
                'return': 'Number Document is used', 
                'id': numberDocument.id,
                'month': numberDocument.month,
                'year': numberDocument.year,
                'status': numberDocument.status
            })
