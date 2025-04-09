import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): # contrato de dados, schema de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True

def capturar_pokemon(id: int) -> PokemonSchema:
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    data = response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
    print(capturar_pokemon(1))
    print(capturar_pokemon(8))
    print(capturar_pokemon(25))
    print(capturar_pokemon(95))
    print(capturar_pokemon(110))