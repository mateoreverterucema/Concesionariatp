import requests
import Concesionaria.src.db.clients_mock

from Concesionaria.src.models.client import ClientAddress

url = 'https://restcountries.com/v2/all'

countries = (requests.get(url)).json()

cc = []

for item in countries:
    list.append(cc, ("Countries name:",item['name'],'-',"Calling Code:",item['callingCodes']))

def get_calling_code(client):
    for country in countries:
        if country["name"] == ClientAddress.countryy:
            return country["callingCodes"][0]

get_calling_code()