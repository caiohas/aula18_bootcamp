import requests

url = "https://pokeapi.co/api/v2/pokemon/15"
response = requests.get(url)
data = response.json()
print(data)