import requests
from pydantic import BaseModel

url = "https://pokeapi.co/api/v2/pokemon/25"

class PokemonSchema(BaseModel): # contrato de dados, schema de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True

response = requests.get(url)
data = response.json()
data_types = data['types']
types_list = []
for type_info in data_types:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list)
print(data['name'], types)