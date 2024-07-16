import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd45eca0f4aab7aa6f051d52090e55ec4'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}

body_create = {
    "name": "generate",
    "photo_id": -1
}

# Создать покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

# Присвоить переменной ID покемона
POKEMON_ID = response_create.json()['id']

# Изменить имя созданного покемона
response_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = {
    "pokemon_id": POKEMON_ID,
    "name": "DeHaviland"
})
print(response_change_name.text)

# Поймать созданного покемона
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = {"pokemon_id": POKEMON_ID})
print(response_catch.text)

# Отправить в нокаут покемона
response_kill = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = {"pokemon_id": POKEMON_ID})
print(response_kill.text)
