import requests
import json

url = 'localhost'
port = '8080'
relationships = '/relationships/'
companies = '/companies/'
numberDocuments = '/numberDocuments/'
print('GET ALL')
get = requests.get('http://'+url+':'+port+relationships)
print(get.json())

print('POST ELEMENT')
print("CAMINHO POSITIVO")

post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355982'})
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355983'})
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355984'})
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355985'})
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355986'})


post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': '01', 'year': '19', 'id_company':'52201001355982'})
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'month': '01', 'year': '19', 'id_company':'52201001355983'})
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010013', 'month': '01', 'year': '19', 'id_company':'52201001355984'})
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010014', 'month': '01', 'year': '19', 'id_company':'52201001355985'})
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010014', 'month': '01', 'year': '19', 'id_company':'52201001355986'})
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010015', 'month': '01', 'year': '19', 'id_company':'52201001355985'})


post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010011', 'id_company': '52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010012', 'id_company': '52201001355982'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010012', 'id_company': '52201001355985'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010013', 'id_company': '52201001355985'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355985'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010015', 'id_company': '52201001355985'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355986'})
print(post.json())

print("CAMINHO NEGATIVO")

print("id_number NULL")
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '', 'id_company': '52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '  ', 'id_company': '52201001355985'})
print(post.json())

print("id_company NULL")
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010012', 'id_company': ''})
print(post.json())
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '  '})
print(post.json())

print("id_number NULL")
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010017', 'id_company': '52201001355983'})
print(post.json())

print("id_company NULL")
post = requests.post('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010012', 'id_company': '52201001355989'})
print(post.json())

print('GET ELEMENT')
print("CAMINHO POSITIVO")

print("by id_company and id_numberDocument")
get = requests.get('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355986'})
print(get.json())
print("by id_company")
get = requests.get('http://'+url+':'+port+relationships,  data={'id_company': '08414996000436'})
print(get.json())
print("by id_numberDocument")
get = requests.get('http://'+url+':'+port+relationships,  data={'id_numberDocument': '522010014'})
print(get.json())

print("CAMINHO NEGATIVO")
print("by id_company inexistente")
get = requests.get('http://'+url+':'+port+relationships,  data={'id_company': '52201001355990'})
print(get.json())
print("by id_numberDocument inexistente")
get = requests.get('http://'+url+':'+port+relationships,  data={'id_numberDocument': '522010020'})
print(get.json())

print("by id_company NULL")
get = requests.get('http://'+url+':'+port+relationships,  data={'id_company': ''})
print(get.json())
get = requests.get('http://'+url+':'+port+relationships,  data={'id_company': ' '})
print(get.json())
print("by id_numberDocument NULL")
get = requests.get('http://'+url+':'+port+relationships,  data={'id_numberDocument': ''})
print(get.json())
get = requests.get('http://'+url+':'+port+relationships,  data={'id_numberDocument': ' '})
print(get.json())

print('PUT ELEMENT')
print("CAMINHO POSITIVO")
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355986', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010011', 'id_company': '52201001355983', 'status': 'Inactive'})
print(put.json())

print("CAMINHO NEGATIVO")
print("Status Null")
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355986', 'status': ' '})
print(put.json())
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355986', 'status': ''})
print(put.json())

print("id_numberDocument inexistente")
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010001', 'id_company': '52201001355986', 'status': 'Inactive'})
print(put.json())

print("id_company inexistente")
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '52201001355980', 'status': 'Inactive'})
print(put.json())

print("id_company Null")
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010014', 'id_company': '   ', 'status': 'Inactive'})
print(put.json())

print("id_numberDocument Null")
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '', 'id_company': '52201001355980', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+relationships, data={'id_numberDocument': '  ', 'id_company': '52201001355980', 'status': 'Inactive'})
print(put.json())


print('GET ALL')
get = requests.get('http://'+url+':'+port+relationships)
print(get.json())

print('DELETE ONE ELEMENT')
print("get")
get = requests.get('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010011', 'id_company': '52201001355983'})
print(get.json())

print("delete")
delete = requests.delete('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010011', 'id_company': '52201001355983'})
print(delete.json())

print("get")
get = requests.get('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010011', 'id_company': '52201001355983'})
print(get.json())

print('DELETE id_company')
delete = requests.delete('http://'+url+':'+port+relationships, data={'id_company': '52201001355983'})
print(delete.json())


print('DELETE id_numberDocument')
delete = requests.delete('http://'+url+':'+port+relationships, data={'id_numberDocument': '522010012'})
print(delete.json())

#print('DELETE ALL ELEMENT')
#delete = requests.delete('http://'+url+':'+port+relationships)
#print(delete.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+relationships)
print(get.json())
