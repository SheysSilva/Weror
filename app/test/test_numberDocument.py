import requests
import json

url = 'localhost'
port = '8080'
numberDocuments='/numberDocuments/'
companies='/companies/'

print('GET ALL')
get = requests.get('http://'+url+':'+port+numberDocuments)
print(get.json())

print('POST ELEMENT')

post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': '01', 'year': '19', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'month': '01', 'year': '19', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010013', 'month': '01', 'year': '19', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010014', 'month': '01', 'year': '19', 'id_company':'52201001355983'})
print(post.json())

#CAMINHO NEGATIVO
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '', 'month': '01', 'year': '19', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010015', 'month': '01', 'year': '', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010015', 'month': '', 'year': '19', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010017', 'month': '01', 'year': '19', 'id_company':''})
print(post.json())

print('GET ONE ELEMENT')
get = requests.get('http://'+url+':'+port+numberDocuments+'522010011')
print(get.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': '03'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010014', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010015', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010015', 'year': '20'})
print(put.json())

#Caminho Negativo
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': ' '})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'year': ' '})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': ' '})
print(put.json())

put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': ''})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'year': ''})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': ''})
print(put.json())


put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': None})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'year': None})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': None})
print(put.json())

put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'month': '02'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': 'Inactive'})
print(put.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+numberDocuments)
print(get.json())

print('DELETE ONE ELEMENT')
delete = requests.delete('http://'+url+':'+port+numberDocuments, data={'id': '522010011'})
print(delete.json())

print('DELETE ALL ELEMENT')
delete = requests.delete('http://'+url+':'+port+numberDocuments)
print(delete.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+numberDocuments)
print(get.json())
