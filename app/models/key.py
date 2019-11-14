from app.db import db

def getKeys():
    chaves = Chaves.query.filter_by(status='Free').limit(64)
    res = {}
    for chave in chaves:
        chave.status = 'Using'
        db.session.commit()

        res[chave.id] = {
            'id': chave.id,
            'status': chave.status
        }          
                
    return jsonify(res)

def getKeyId(id):
    if isNull(id):
        return jsonify({'return':'Id is Null!'})

    chave = Chaves.query.filter_by(id=str(id)).first()

    if not chave:
        return jsonify({'return':'Key not exist!'})
    res = {
        'id': chave.id,
        'status': chave.status
    }

    return jsonify(res)

def postKey(id):
    if isNull(id):
        return jsonify({'return':'ID null!'})

    chave = Chaves.query.filter_by(id=str(id)).first()

    if not chave:
        chave = Chaves(str(id))
        db.session.add(chave)
        db.session.commit()
        return jsonify({'id': chave.id})

    return jsonify({'return': 'Exist object'})

def putKey(id, status):
    if isNull(id) or isNull(status):
        return jsonify({'return':'Values Null!'})

    chave = Chaves.query.filter_by(id=id).first()
        
    if not chave:
        return jsonify({'return': 'Not Exist'})
    else:
        chave.status = str(status)
        db.session.commit()
        chave = Chaves.query.filter_by(id=id).first()
        return jsonify({'id': chave.id, 'status': chave.status})

def deleteKey(id):
    if isNull(id): 
        return deleteKeys()
    else:
        chave = Chaves.query.filter_by(id=id).first()
            
        if not chave:
            return jsonify({'return': 'Not Exist'})
        else:
            if chave.status == 'Ok':
                db.session.delete(chave)
                db.session.commit()
                return jsonify({'return':'Success', 'id': chave.id, 'status': chave.status})
        
            return jsonify({'return': 'Key not used', 'id': chave.id, 'status': chave.status})

def deleteKeys():
    chaves = Chaves.query.filter_by(status='Ok')
    for chave in chaves:
        db.session.delete(chave)
        db.session.commit()
    return jsonify({'return':'Success'})