import requests
import json

url = 'localhost'
port = '8080'
numberDocuments = '/numberDocuments/'

print('GET ALL')
get = requests.get('http://'+url+':'+port+numberDocuments)
print(get.json())

print('POST ELEMENT')

post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010011', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010013', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010014', 'id_company':'52201001355983'})
print(post.json())

#CAMINHO NEGATIVO
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '', 'id_company':'52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010017', 'id_company':''})
print(post.json())
post = requests.post('http://'+url+':'+port+numberDocuments, data={'id': '522010017', 'id_company':'52201001355990'})
print(post.json())

print('GET ONE ELEMENT')
get = requests.get('http://'+url+':'+port+numberDocuments+'522010011')
print(get.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010014', 'status': 'Inactive'})
print(put.json())
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010015', 'status': 'Inactive'})
print(put.json())

#Caminho Negativo
put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': ' '})
print(put.json())

put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': ''})
print(put.json())

put = requests.put('http://'+url+':'+port+numberDocuments, data={'id': '522010012', 'status': None})
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
