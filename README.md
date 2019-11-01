# Weror
###### Empresa: **Contagil**

API com chaves de notas fiscais para uso interno da empresa Contagil. 

## Migrar o banco de dados

```
flask db migrate
```
## Atualizar o banco de dados

```
flask db upgrade
```

## Rodar o projeto localmente

```
flask run
```

## Rodar o projeto para acesso remoto

```
flask run --host=0.0.0.0 --port=80
```

## Rodar os Testes

```
python test.py
```

## Status das Chaves

As chaves possuem quatro estados diferentes:

- (Using): Chave em uso.
- (Free): Chave disponivel para uso.
- (Ok): Chave já foi usada em outra consulta.
- (Bloqued): Chave está bloqueada para uso.

###### Site: [Contagil](http://www.contagilpb.com.br/)
