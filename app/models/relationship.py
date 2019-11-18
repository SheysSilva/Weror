from app.db import db
from flask import jsonify
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
	res = {}
	for rel in relationships:
		res[count] = {
            'id_company': rel.id_company,
            'id_numberDocument': rel.id_numberDocument
        }

		count = count + 1
	return jsonify(res)


def getOneRelationship(id_company, id_numberDocument):
	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
	if not relationship:
		return jsonify({'return': 'Not Exist Relationship'})

	return jsonify({
		'id_company': relationship.id_company, 
		'id_numberDocument': relationship.id_numberDocument,
		'status': relationship.status
	})

def getRelationshipCompanyId(id_company):
	relationships = Relationship.query.filter_by(id_company=str(id_company))
	res = {}
	for rel in relationships:
		res[rel.id_numberDocument]={
			'id_company': rel.id_company,
			'id_numberDocument': rel.id_numberDocument,
			'status': rel.status
		}
	return jsonify(res)

def getRelationshipNumberDocumentId(id_numberDocument):
	relationships = Relationship.query.filter_by(id_numberDocument=str(id_numberDocument))
	res = {}
	for rel in relationships:
		res[rel.id_company]={
			'id_company': rel.id_company, 
			'id_numberDocument': rel.id_numberDocument,
			'status': rel.status
		}

	return jsonify(res)

def postRelationship(id_company, id_numberDocument):
	if isNull(id_company) or isNull(id_numberDocument):
		return jsonify({'return':'Values null!'})

	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()

	if not relationship:
		_company = Company.query.filter_by(id=str(id_company)).first()

		if not _company:
			return jsonify({'return': 'Not exist company'})

		_numberDocument = NumberDocument.query.filter_by(id=str(id_numberDocument)).first()

		if not _numberDocument:
			return jsonify({'return': 'Not exist number document'})

		relationship = Relationship(str(id_company), str(id_numberDocument))
		db.session.add(relationship)
		db.session.commit()

		return jsonify({
			'id_company': relationship.id_company, 
			'id_numberDocument': relationship.id_numberDocument,
			'status': relationship.status
		})

	return jsonify({'return': 'Exist Relationship'})
 

def putRelationship(id_company, id_numberDocument, status):
	if isNull(id_company) or isNull(id_numberDocument) or isNull(status):
		return jsonify({'return':'Values is Null'})

	relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
        
	if not relationship:
		return jsonify({'return': 'Not Exist'})
	else:
		relationship.status = str(status)
		db.session.commit()
		
		rel = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
		if not rel:
			return jsonify({'return': 'Not Exist'})
		return jsonify({
			'id_company': rel.id_company, 
			'id_numberDocument': rel.id_numberDocument,
			'status': rel.status
		})

def deleteRelationship(id_company, id_numberDocument):
	if not isNull(id_company) and not isNull(id_numberDocument):
		relationship = Relationship.query.filter_by(id_company=str(id_company), id_numberDocument=str(id_numberDocument)).first()
		if not not relationship:
			db.session.delete(relationship)
			db.session.commit()
		return jsonify({'return': 'Success'})

	if not isNull(id_company) and isNull(id_numberDocument):
		return deleteRelationshipCompanyId(id_company)
	if isNull(id_company) and not isNull(id_numberDocument):
		return deleteRelationshipNumberDocumentId(id_numberDocument)
	
	return jsonify({'return': 'Values is Null'})

def deleteRelationshipCompanyId(id_company):
	relationship = Relationship.query.filter_by(id_company=str(id_company)).first()
	for rel in relationship:
		db.session.delete(rel)
		db.session.commit()

	return jsonify({'return': 'Success'})

def deleteRelationshipNumberDocumentId(id_numberDocument):
	relationship = Relationship.query.filter_by(id_numberDocument=str(id_numberDocument)).first()
	for rel in relationship:
		db.session.delete(rel)
		db.session.commit()

	return jsonify({'return': 'Success'})



    