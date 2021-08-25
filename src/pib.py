import requests
import pandas

nivel = "N6"

localidade = {
    "N6": "municipio",
    "N8": "mesorregiao"
}

regiao = localidade[nivel]

URL = f'https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2018/variaveis/37?localidades={nivel}[all]'

r = requests.get(URL)
response = r.json()

array = []
for res in response:
    for j in res['resultados']:
        for s in j['series']:
            dict = {}
            dict[f'id_{regiao}'] = s['localidade']['id']
            dict['pib'] = s['serie']['2018']
            array.append(dict)

df = pandas.DataFrame.from_dict(array)
df.to_csv(f'pib_{regiao}.csv', index=False)