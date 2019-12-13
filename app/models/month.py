from app.db import db
from flask import jsonify, make_response
import json
from app.util.util import *
from app.models.models import *

def getMonths():
    months = Month.query.all()
    res = []
    for month in months:
        res.append({
            'id': month.id,
            'state': month.state,            
            'year': month.year,
            'company_id': month.company_id,
            'serie': month.serie,
            'issue': month.issue,
            'model': month.model,
            'inicial': month.inicial,
            'returns': month.returns
        })          
                
    return make_response(jsonify(res), 200)

def getMonthCompanyId(company_id):
    res = []
    min_id = db.session.query(db.func.min(Month.id)).scalar()
    min_year = db.session.query(db.func.min(Month.year)).scalar()
    months = Month.query.filter_by(id=str(min_id), year=str(min_year), returns=0, inicial=1, company_id=str(company_id))
    for month in months:
        res.append({
            'id': month.id,
            'state': month.state,
            'year': month.year,
            'serie': month.serie,
            'issue': month.issue,
            'model': month.model,
            'inicial': month.inicial,
            'returns': month.returns
        })     
                        
    return make_response(jsonify(res), 200)

def getMonth(id):
    res = []
    months = Month.query.filter_by(id=str(id))
    for month in months:
        res.append({
            'id': month.id,
            'state': month.state,
            'year': month.year,
            'company_id': month.company_id,
            'serie': month.serie,
            'issue': month.issue,
            'model': month.model,
            'inicial': month.inicial,
            'returns': month.returns
        })     
                        
    return make_response(jsonify(res), 200)

def getMonthId(id, company_id):
    if isNull(id):
        return make_response(jsonify({'return':'Id is Null!'}), 406)

    month = Month.query.filter_by(id=str(id), company_id=str(company_id)).first()

    if not month:
        return make_response(jsonify({'return':'Month not exist!'}), 204)
    res = {
        'id': month.id,
        'state': month.state,
        'year': month.year,
        'company_id': month.company_id,
        'serie': month.serie,
        'issue': month.issue,
        'model': month.model,
        'inicial': month.inicial,
        'returns': month.returns
    }

    return make_response(jsonify(res), 200)

def postMonth(id, year, serie, model, issue, state, inicial, company_id):
    if isNull(id) or isNull(year) or isNull(model) or isNull(serie) or isNull(issue) or isNull(state) or isNull(company_id):
        return make_response(jsonify({'return':'ID null!'}), 406)

    month = Month.query.filter_by(id=str(id), year=str(year), serie=str(serie), model=str(model), issue=str(issue), state=str(state), company_id=str(company_id)).first()

    if not month:
        company = Company.query.filter_by(id=str(company_id)).first()

        if not company:
            return make_response(jsonify({'return': 'Company not exist'}), 204)

        if inicial==None:
            inicial=1

        month = Month(str(id), str(year), str(serie), str(model), str(issue), str(state), int(inicial), str(company_id))

        db.session.add(month)
        db.session.commit()
        return make_response(jsonify({'id': month.id}), 201)

    return make_response(jsonify({'return': 'Exist object'}), 200)

def putMonth(id, returns):
    if isNull(id) or isNull(returns):
        return make_response(jsonify({'return':'Values Null!'}), 406)

    month = Month.query.filter_by(id=id).first()
        
    if not month:
        return make_response(jsonify({'return': 'Not Exist'}), 204)
    else:
        month.returns = str(returns)
        db.session.commit()
        month = Month.query.filter_by(id=id).first()
        return make_response(jsonify({'id': month.id, 'returns': month.returns}), 200)

def deleteMonth(id, company_id):
    if isNull(id): 
        return deleteMonths()
    else:
        month = Month.query.filter_by(id=id, company_id=str(company_id)).first()
            
        if not month:
            return make_response(jsonify({'return': 'Not Exist'}), 204)
        else:
            db.session.delete(month)
            db.session.commit()
            return make_response(jsonify({
                'return':'Success', 
                'id': month.id,
                'state': month.state,
                'year': month.year,                
                'company_id': month.company_id,
                'serie': month.serie,
                'issue': month.issue,
                'model': month.model,
                'inicial': month.inicial,
                'returns': month.returns})
            , 200)                        
            

def deleteMonths():
    for month in months:
        db.session.delete(month)
        db.session.commit()
    return make_response(jsonify({'return':'Success'}), 200)