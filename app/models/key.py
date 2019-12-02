from app.db import db
from flask import jsonify, make_response
from app.util.util import *
from app.models.models import *

def getKeys():
    keys = Keys.query.filter_by(status='Free').limit(64)
    res = []
    for key in keys:
        key.status = 'Using'
        db.session.commit()

        res.append({
            'id': key.id,
            'status': key.status
        })          
                
    return make_response(jsonify(res), 200)

def getKeyId(id):
    if isNull(id):
        return make_response(jsonify({'return':'Id is Null!'}), 406)

    key = Keys.query.filter_by(id=str(id)).first()

    if not key:
        return make_response(jsonify({'return':'Key not exist!'}), 204)
    res = {
        'id': key.id,
        'status': key.status
    }

    return make_response(jsonify(res), 200)

def postKey(id, state, year, month, model, serie, issue, numberDocumentId):
    if isNull(id) or isNull(uf) or isNull(year) or isNull(month) or isNull(model) or isNull(serie) or isNull(issue) or isNull(numberDocumentId):
        return make_response(jsonify({'return':'ID null!'}), 406)

    key = Keys.query.filter_by(id=str(id)).first()

    if not key:
        numberDocument = NumberDocument.query.filter_by(id=str(numberDocumentId)).first()

        if not numberDocument:
            return make_response(jsonify({'return': 'Number Document not exist'}), 204)

        key = Keys(str(id), str(state), str(year), str(month), str(model), str(serie), str(issue), str(numberDocumentId))
        db.session.add(key)
        db.session.commit()
        return make_response(jsonify({'id': key.id}), 201)

    return make_response(jsonify({'return': 'Exist object'}), 200)

def putKey(id, status):
    if isNull(id) or isNull(status):
        return make_response(jsonify({'return':'Values Null!'}), 406)

    key = Keys.query.filter_by(id=id).first()
        
    if not key:
        return make_response(jsonify({'return': 'Not Exist'}), 204)
    else:
        key.status = str(status)
        db.session.commit()
        key = Keys.query.filter_by(id=id).first()
        return make_response(jsonify({'id': key.id, 'status': key.status}), 200)

def deleteKey(id):
    if isNull(id): 
        return deleteKeys()
    else:
        key = Keys.query.filter_by(id=id).first()
            
        if not key:
            return make_response(jsonify({'return': 'Not Exist'}), 204)
        else:
            if key.status == 'Ok':
                db.session.delete(key)
                db.session.commit()
                return make_response(jsonify({'return':'Success', 'id': key.id, 'status': key.status}), 200)
        
            return make_response(jsonify({'return': 'Key not used', 'id': key.id, 'status': key.status}), 200)

def deleteKeys():
    keys = Keys.query.filter_by(status='Ok')
    for key in keys:
        db.session.delete(key)
        db.session.commit()
    return make_response(jsonify({'return':'Success'}), 200)