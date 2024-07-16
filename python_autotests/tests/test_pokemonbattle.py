import requests
import pytest

TRAINER_ID = '4736'
TRAINER_NAME = 'Nortrop'
URL = 'https://api.pokemonbattle.ru/v2/trainers?trainer_id=' + TRAINER_ID
TOKEN = 'd45eca0f4aab7aa6f051d52090e55ec4'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
}

def test_status_code():
    response = requests.get(url = URL, headers = HEADER)
    assert response.status_code == 200

def test_trainer_name_code():
    response = requests.get(url = URL, headers = HEADER)
    assert response.json()['data'][0]['trainer_name'] == 'Nortrop'