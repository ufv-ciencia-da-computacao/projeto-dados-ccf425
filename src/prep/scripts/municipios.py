import requests
import pandas

URL = r'https://servicodados.ibge.gov.br/api/v1/localidades/regioes/3/municipios'

r = requests.get(URL)
response = r.json()

array = []

for j in response:
    dict = {}
    dict['id'] = j['id']
    dict['nome'] = j['nome']
    dict['microrregiao_id'] = j['microrregiao']['id']
    dict['microrregiao_nome'] = j['microrregiao']['nome']
    dict['mesorregiao_id'] = j['microrregiao']['mesorregiao']['id']
    dict['mesorregiao_nome'] = j['microrregiao']['mesorregiao']['nome']
    dict['UF'] = j['microrregiao']['mesorregiao']['UF']['sigla']
    dict['UF_nome'] = j['microrregiao']['mesorregiao']['UF']['nome']
    dict['regiao'] = j['microrregiao']['mesorregiao']['UF']['regiao']['nome']
    dict['regiao-imediata_id'] = j['regiao-imediata']['id']
    dict['regiao-imediata_nome'] = j['regiao-imediata']['nome']
    dict['regiao-intermediaria_id'] = j['regiao-imediata']['regiao-intermediaria']['id']
    dict['regiao-intermediaria_nome'] = j['regiao-imediata']['regiao-intermediaria']['nome']

    array.append(dict)

df = pandas.DataFrame.from_dict(array)
df.to_csv('municipios.csv', index=False)
