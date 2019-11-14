from app.db import db
from app.util.util import *

def postRelationship(id_company, id_numberDocument):
	if isNull(id_company) and isNull(id_numberDocument):
		return jsonify({'return':'Values null!'})
	else:
		relationship = Relationship(str(id_company), str(id_numberDocument))
		db.session.add(relationship)
		db.session.commit()

		return jsonify({
			'id_company': relationship.id_company, 
			'id_numberDocument': relationship.id_numberDocument,
			'status': relationship.status
		})

def putRelationship(id_company, id_numberDocument, status):
	if isNull(id_company) and isNull(id_numberDocument) and isNull(status):
		return jsonify({'return':'Values is Null'})

	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
        
	if not relationship:
		return jsonify({'return': 'Not Exist'})
	else:
		relationship.status = str(status)
		db.session.commit()
		relationship = getOneRelationship(id_company, id_numberDocument)
		return jsonify({
			'id_company': relationship.id_company, 
			'id_numberDocument': relationship.id_numberDocument,
			'status': relationship.status
		})

def getOneRelationship(id_company, id_numberDocument):
	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
	return jsonify({
		'id_company': relationship.id_company, 
		'id_numberDocument': relationship.id_numberDocument,
		'status': relationship.status
	})

def getRelationshipCompanyId(id_company):
	relationship = Relationship.query.filter_by(id_company=str(id_company)).first()
	res = {}
	for rel in relationship:
		res[rel.id_numberDocument]={
			'id_numberDocument': relationship.id_numberDocument,
			'status': relationship.status
		}
	return jsonify(res)

def getRelationshipNumberDocumentId(id_numberDocument):
	relationship = Relationship.query.filter_by(id_numberDocument=str(id_numberDocument)).first()
	res = {}
	for rel in relationship:
		res[rel.id_company]={
			'id_company': relationship.id_company, 
			'status': relationship.status
		}
	return jsonify(res)
    