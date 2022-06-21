import json
from Concesionaria.src.models.car import Specs_autos, Motor


def load_cars():
    cars = []

    with open('Concesionaria/src/db/car_models.json', 'r') as file:
        cars_json = json.load(file)
        for car in cars_json:
            cars.append(
                Specs_autos(
                    car['id'],
                    car['model'],
                    car['price'],
                    car['body'],
                    car['transmission'],
                    car['power'],
                    car['fuel'],
                    car['top speed'],
                    car['acceleration 0-100km/h'],
                    Motor(
                        car["motor"]['cylinders'],
                        car["motor"]['valves per cylinder'],
                        car["motor"]['turbo'],
                        car["motor"]['fuel tank capacity'])
                )
            )
    return cars
