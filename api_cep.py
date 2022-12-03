import requests
import json

cep = "12916-560"

r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
print(r.json())