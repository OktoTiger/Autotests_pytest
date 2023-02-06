import requests
import pytest

def test_status_code ():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

@pytest.mark.parametrize('key,value', [('trainer_name','Орел')])

def test_trainer (key, value):
    response_trainer = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id':'1894'})
    assert response_trainer.json()[key] == value

 