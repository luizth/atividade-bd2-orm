import requests

import config


def get_headers():
    return {"Content-type": "application/json", "Accept": "application/json"}


def test_api_create_cliente():  # execute app.py antes de rodar os testes
    url = config.get_api_url()
    cliente_data = {
        "nome": "João",
        "idade": 26,
        "sexo": "M"
    }
    res = requests.post(url + '/cliente', json=cliente_data, headers=get_headers())
    assert res.status_code == 200
