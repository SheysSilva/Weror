# Weror
###### Empresa: **Contagil**

API com chaves de notas fiscais para uso interno da empresa Contagil. 

## Configuração Inicial

```
export FLASK_CONFIG=development
export FLASK_APP=run.py
```

## Iniciar o banco de dados

```
flask db init
```

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
flask run --host=0.0.0.0 --port=8080
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
