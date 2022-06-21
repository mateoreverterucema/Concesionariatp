from flask import jsonify
import json
from Concesionaria.main import clients


def store_client_file():
    with open('Concesionaria/src/db/test.json', 'w') as store_file:
        clients_json = jsonify(eqtls=[element.serialize() for element in clients])
        json.dump(clients_json, store_file)
        print(f"client stored")
