import requests
import json

url = 'localhost'
port = '8080'
print('GET ALL')
get = requests.get('http://'+url+':'+port+'/chaves/')
print(get.json())

print('POST ELEMENT')
post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355982'})
print(post.json())
post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355983'})
print(post.json())
post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355984'})
print(post.json())
post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355985'})
print(post.json())

print('GET ONE ELEMENT')
get = requests.get('http://'+url+':'+port+'/chaves/25190908414996000193650040002952201001355982')
print(get.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355982'})
print(put.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355982', 'status': ''})
print(put.json())

print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355982', 'status': ' '})
print(put.json())


print('PUT ELEMENT')
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355982', 'status': 'Ok'})
print(put.json())
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355983', 'status': 'OK'})
print(put.json())
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355984', 'status': 'OK'})
print(put.json())
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355985', 'status': 'OK'})
print(put.json())
put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355984', 'status': 'OK'})
print(put.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+'/chaves/')
print(get.json())

print('DELETE ONE ELEMENT')
delete = requests.delete('http://'+url+':'+port+'/chaves/', data={'id': '25190908414996000193650040002952201001355982'})
print(delete.json())

print('DELETE ALL ELEMENT')
delete = requests.delete('http://'+url+':'+port+'/chaves/')
print(delete.json())

print('GET ALL')
get = requests.get('http://'+url+':'+port+'/chaves/')
print(get.json())
