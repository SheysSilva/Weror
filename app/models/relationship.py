from app.db import db
from flask import jsonify,make_response
from app.util.util import *
from app.models.models import *

def getRelationship(id_company, id_numberDocument):
	if isNull(id_company) and isNull(id_numberDocument):
		return getAllRelationship()
	if not isNull(id_company) and not isNull(id_numberDocument):
		return getOneRelationship(id_company, id_numberDocument)
	if not isNull(id_company) :
		return getRelationshipCompanyId(id_company)
	if isNull(id_company) :
		return getRelationshipNumberDocumentId(id_numberDocument)

def getAllRelationship():
	relationships = Relationship.query.all()
	count = 0
	res = []
	for rel in relationships:
		res.append({
            'id_company': rel.id_company,
            'id_numberDocument': rel.id_numberDocument
        })

		count = count + 1
	return make_response(jsonify(res), 200)


def getOneRelationship(id_company, id_numberDocument):
	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
	if not relationship:
		return make_response(jsonify({'return': 'Not Exist Relationship'}), 204)

	return make_response(jsonify({
		'id_company': relationship.id_company, 
		'id_numberDocument': relationship.id_numberDocument,
		'status': relationship.status
	}), 200)

def getRelationshipCompanyId(id_company):
	relationships = Relationship.query.filter_by(id_company=str(id_company))
	res = []
	for rel in relationships:
		res.append({
			'id_company': rel.id_company,
			'id_numberDocument': rel.id_numberDocument,
			'status': rel.status
		})
	return make_response(jsonify(res), 200)

def getRelationshipNumberDocumentId(id_numberDocument):
	relationships = Relationship.query.filter_by(id_numberDocument=str(id_numberDocument))
	res = []
	for rel in relationships:
		res.append({
			'id_company': rel.id_company, 
			'id_numberDocument': rel.id_numberDocument,
			'status': rel.status
		})

	return make_response(jsonify(res), 200)

def postRelationship(id_company, id_numberDocument):
	if isNull(id_company) or isNull(id_numberDocument):
		return make_response(jsonify({'return':'Values null!'}), 406)

	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()

	if not relationship:
		_company = Company.query.filter_by(id=str(id_company)).first()

		if not _company:
			return make_response(jsonify({'return': 'Not exist company'}), 204)

		_numberDocument = NumberDocument.query.filter_by(id=str(id_numberDocument)).first()

		if not _numberDocument:
			return make_response(jsonify({'return': 'Not exist number document'}), 204)

		relationship = Relationship(str(id_company), str(id_numberDocument))
		db.session.add(relationship)
		db.session.commit()

		return make_response(jsonify({
			'id_company': relationship.id_company, 
			'id_numberDocument': relationship.id_numberDocument,
			'status': relationship.status
		}), 201)

	return make_response(jsonify({'return': 'Exist Relationship'}), 200)
 

def putRelationship(id_company, id_numberDocument, status):
	if isNull(id_company) or isNull(id_numberDocument) or isNull(status):
		return make_response(jsonify({'return':'Values is Null'}), 406)

	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
        
	if not relationship:
		return make_response(jsonify({'return': 'Not Exist'}), 204)
	else:
		relationship.status = str(status)
		db.session.commit()
		
		rel = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
		if not rel:
			return make_response(jsonify({'return': 'Not Exist'}), 204)

		return make_response(jsonify({
			'id_company': rel.id_company, 
			'id_numberDocument': rel.id_numberDocument,
			'status': rel.status
		}), 200)

def deleteRelationship(id_company, id_numberDocument):
	if not isNull(id_company) and not isNull(id_numberDocument):
		rel = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument))
		if not rel:
			return make_response(jsonify({'return': 'Relationship not exist'}), 204)
		
		db.session.delete(rel)
		db.session.commit()
		return make_response(jsonify({'return': 'Success'}), 200)

	if not isNull(id_company):
		return deleteRelationshipCompanyId(id_company)
	if not isNull(id_numberDocument):
		return deleteRelationshipNumberDocumentId(id_numberDocument)
	
	return jsonify({'return': 'Values is Null'})

def deleteRelationshipCompanyId(id_company):
	relationship = Relationship.query.filter_by(id_company=str(id_company))
	for rel in relationship:
		db.session.delete(rel)
		db.session.commit()

	return make_response(jsonify({'return': 'Success'}), 200)

def deleteRelationshipNumberDocumentId(id_numberDocument):
	relationship = Relationship.query.filter_by(id_numberDocument=str(id_numberDocument))
	for rel in relationship:
		db.session.delete(rel)
		db.session.commit()

	return make_response(jsonify({'return': 'Success'}), 200)



    