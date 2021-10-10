import requests
import pandas

nivel = "N8"

localidade = {
    "N6": "municipio",
    "N8": "mesorregiao"
}

regiao = localidade[nivel]

URL = f'https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/2010/variaveis/616?localidades={nivel}[all]'

r = requests.get(URL)
response = r.json()

array = []
for res in response:
    for j in res['resultados']:
        for s in j['series']:
            dict = {}
            dict[f'id_{regiao}'] = s['localidade']['id']
            dict['densidade'] = s['serie']['2010']
            array.append(dict)

df = pandas.DataFrame.from_dict(array)
df.to_csv(f'densidade_{regiao}.csv', index=False)