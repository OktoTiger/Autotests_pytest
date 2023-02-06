import requests
import json 

token = 'bcc22b705a199d33453cf8c7d20fdf07'


# 1.Создание покемона 
response_create_pokemon = requests.post('https://pokemonbattle.me:5000/pokemons',
 json={
    "name": "Шмель",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
}, headers={'Content-Type': 'application/json', 'trainer_token': token})
print (response_create_pokemon.text)

# 2.Смена имени покемона 
pokemon_id = response_create_pokemon.json()['id']

response_change = requests.put ('https://pokemonbattle.me:5000/pokemons',
 json={
    "pokemon_id": pokemon_id,
    "name": "Шершень",
    "photo": ""
}, headers={'Content-Type': 'application/json', 'trainer_token': token})
print (response_change.text)

# 3.Поймать покемона в покетбол (3046,3047)

response_caght_pokemon = requests.post('https://pokemonbattle.me:5000//trainers/add_pokeball',
json={
    "pokemon_id": pokemon_id
}, headers={'Content-Type': 'application/json', 'trainer_token': token})
print (response_caght_pokemon.text)


