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
flask run --host=0.0.0.0 --port=8081
```

## Rodar os Testes

```
python test.py
```

### Status das Chaves

As chaves possuem quatro estados diferentes:

- (Using): Chave em uso.
- (Free): Chave disponivel para uso.
- (Ok): Chave já foi usada em outra consulta.
- (Bloqued): Chave está bloqueada para uso.

### Status das Empresas(Companies)

As Empresas possuem quatro estados diferentes:

- (Active): Pode gerar chaves para o CNPJ dessa empresa.
- (Inactive): A empresa está empedida de gerar chaves.
- (Bloqued): A empresa não irá gerar chaves por um tempo determinado.

### Status do Numeros de Documento(Number Documents)

Os Numeros de Documentos possuem quatro estados diferentes:

- (Active): Gerou nota
- (Inactive): Não gerou nota
- (Bloqued): Ainda vai gerar nota

_Cada Numero de Documento possui uma relação com a Empresa, onde essa relação possui um status_

## Relação entre Numero de Documento(Number Document) e Empresa(Company)

| id_company     | id_numberDocument | status |
|----------------|-------------------|--------|
| 52201001355983 | 522010011         | Active |
| 52201001355983 | 522010013         | Active |
| 52201001355983 | 522010014         | Active |

### Status da Relação

- (Active): Esta gerando notas.
- (Inactive): Não gera mais notas.

###### Site: [Contagil](http://www.contagilpb.com.br/)
