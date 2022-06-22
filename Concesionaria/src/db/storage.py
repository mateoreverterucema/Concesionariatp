import json


def store_client_file(clients_list):
    with open('Concesionaria/src/db/clients_test.json', 'w') as store_file:
        json.dump(clients_list, store_file)
        print(f"clients stored")


def store_car_file(cars_list):
    with open('Concesionaria/src/db/cars_test.json', 'w') as store_file:
        json.dump(cars_list, store_file)
        print(f"cars stored")


def store_purchase_file(purchase_list):
    with open('Concesionaria/src/db/purchase_orders_test.json', 'w') as store_file:
        json.dump(purchase_list, store_file)
        print(f"purchase/s stored")
