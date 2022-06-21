import json
from flask import Flask
from flask import request
import requests
from flask import jsonify
from Concesionaria.src.models.client import Client, ClientAddress, ClientPhoneNumber, id_generator
from Concesionaria.src.models.car import Motor, Specs_autos
from Concesionaria.src.models.purchase_order import Purchase_order
from Concesionaria.src.db.client_loader import load_clients
from Concesionaria.src.db.car_loader import load_cars

app = Flask(__name__)
clients: list = load_clients()
cars: list = load_cars()
purchase_order: list = []


# Internal use
@app.route("/api/concesionaria/clients/", methods=['GET'])
def get_all_clients():
    return jsonify([client.serialize() for client in clients])


@app.route("/api/concesionaria/clients/<client_id>", methods=['GET'])
def get_client(client_id):
    for client in clients:
        if client.id == client_id:
            return jsonify(client.serialize())


@app.route("/api/concesionaria/clients/", methods=['POST'])
def create_client():
    client = request.json

    try:
        new_client = Client(
            id_generator(),
            client['date_created'],
            client['first_name'],
            client['last_name'],
            client['date_of_birth'],
            client['gender'],
            ClientPhoneNumber(
                client["phone_number"]["calling_code"],
                client["phone_number"]["phone_number"]
            ),
            client['email'],
            client['client_status'],
            ClientAddress(
                client['client_address']['street'],
                client['client_address']['street_number'],
                client['client_address']['city'],
                client['client_address']['state'],
                client['client_address']['post_code'],
                client['client_address']['country']
            )
        )

        clients.append(new_client)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_client.serialize())


@app.route("/api/concesionaria/cars/", methods=['GET'])
def get_all_cars():
    return jsonify([car.serialize() for car in cars])


@app.route("/api/concesionaria/cars/<car_id>", methods=['GET'])

def car_image(car_id):
    for car in cars:
        if car.id == car_id:
            url = "https://google-image-search1.p.rapidapi.com/v2/"

            querystring = {"q": str(car.model), "hl": "en", "pageNumber": "1", "pageSize": "10", "autoCorrect": "true"}

            headers = {
                "X-RapidAPI-Key": "6fb3a57ecemsh3faac6f662be92dp10e7b3jsn35ff00c16d10",
                "X-RapidAPI-Host": "google-image-search1.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            return response.text

@app.route("/api/concesionaria/cars/", methods=['POST'])
def create_car():
    car = request.json

    try:
        new_car = Specs_autos(
            id_generator(),
            car['model'],
            car['price'],
            car['body'],
            car['transmission'],
            car['power'],
            car['fuel'],
            car['top_speed'],
            car['acceleration_0_100kmh'],
            Motor(
                car["motor"]["cilynders"],
                car["motor"]["valves_per_cilynder"],
                car["moto"]["turbo"],
                car["moto"]["fuel_tank_capacity"]
            )
        )
        cars.append(new_car)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_car.serialize())


@app.route("/api/concesionaria/cars/<car_id>", methods=['PUT'])
def change_price(car_id, new_price):
    for car in cars:
        if car.id == car_id:
            car.price = new_price

    return get_car(car_id)


@app.route("/api/concesionaria/cars/<car_id>", methods=['DELETE'])
def delete_car(car_id):
    for car in cars:
        if car.id == car_id:
            cars.remove(car)

    return cars


@app.route("/api/concesionaria/cars/purchase_orders", methods=['GET'])
def load_purchase_order():
    purchase_orders = []

    with open('Concesionaria/src/db/purchase_orders.json', 'r') as file:
        purchase_orders_json = json.load(file)
        for purch_order in purchase_orders_json:
            purchase_orders.append(
                Purchase_order(
                    purch_order['id'],
                    purch_order['purchase_number'],
                    purch_order['amount'],
                    purch_order['car_model'],
                )
            )
    return purchase_orders


@app.route("/api/concesionaria/client_test", methods=['POST'])
def store_client_file(clients_list):
    with open('Concesionaria/src/db/test.json', 'w') as store_file:
        json.dump(clients_list, store_file)
        print(f"client stored")

@app.route("/api/concesionaria/clients/<client_id>", methods=['GET'])
def delete_client(client_id):
    for client in clients:
        if client_id == client.id:
            client.client_status = "NOT ACTIVE"
            return client
