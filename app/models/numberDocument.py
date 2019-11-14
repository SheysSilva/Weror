from app.db import db
from app.util.util import *
    ### Number Document ###

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

    def putNumberDocument(id, month, year, status):
      

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
