import requests
import json

url = 'localhost'
port = '8080'
companies ='/companies/'

print('GET ALL')
get = requests.get('http://'+url+':'+port+companies)
print(get.json())

print('POST ELEMENT')
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355982'})
print(post.json())
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355984'})
print(post.json())
post = requests.post('http://'+url+':'+port+companies, data={'id': '52201001355985'})
print(post.json())

print('GET ONE ELEMENT')
get = requests.get('http://'+url+':'+port+companies+'52201001355983')
print(get.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355982'})
print(put.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355982', 'status': ''})
print(put.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355982', 'status': ' '})
print(put.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355982', 'status': 'Active'})
print(put.json())
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355983', 'status': 'Active'})
print(put.json())
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355984', 'status': 'Active'})
print(put.json())
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355985', 'status': 'Active'})
print(put.json())
put = requests.put('http://'+url+':'+port+companies, data={'id': '52201001355984', 'status': 'Active'})
print(put.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+companies)
print(get.json())

print('DELETE ONE ELEMENT')
delete = requests.delete('http://'+url+':'+port+companies, data={'id': '52201001355982'})
print(delete.json())

print('DELETE ALL ELEMENT')
delete = requests.delete('http://'+url+':'+port+companies)
print(delete.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+companies)
print(get.json())
