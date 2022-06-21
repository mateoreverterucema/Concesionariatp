import json
from Concesionaria.src.models.car import Specs_autos, Motor


def load_cars():
    cars = []

    with open('Concesionaria/src/db/car_models.json', 'r') as file:
        cars_json = json.load(file)
        for car in cars_json:
            cars.append(
                Specs_autos(
                    car['model'],
                    car['price'],
                    car['body'],
                    car['transmission'],
                    car['power'],
                    car['fuel'],
                    car['top_speed'],
                    car['acceleration_0_100kmh'],
                    Motor(
                        car['cylinders'],
                        car['valves_per_cylinder'],
                        car['turbo'],
                        car['fuel_tank_capacity']
                    )
                )
            )
    return cars