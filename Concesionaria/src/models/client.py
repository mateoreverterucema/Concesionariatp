import json
import uuid


def store_client_file(client):
    with open('src/db/test.json', 'w') as store_file:
        json.dump(client, store_file)
        print(f"Client stored")


def id_generator():
    return str(uuid.uuid4())


class Client:

    def __init__(self, id, date_created, first_name, last_name, date_of_birth, gender, phone_number, email,
                 client_status, client_address) -> None:
        self.id = id
        self.date_created = date_created
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.client_status = client_status
        self.address = client_address

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'client_status': self.client_status,
            'data_created': self.date_created,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth,
            'phone_number': self.phone_number.serialize(),
            'address': self.address.serialize()
        }


class ClientPhoneNumber:

    def __init__(self, calling_code, phone_number) -> None:
        self.calling_code = calling_code
        self.phone_number = phone_number

    def serialize(self):
        return {
            'calling_code': self.calling_code,
            'phone_number': self.phone_number
        }


class ClientAddress:


    def __init__(self, street, street_number, city, state, post_code, country) -> None:
        self.street = street
        self.street_number = street_number
        self.city = city
        self.state = state
        self.post_code = post_code
        self.country = country

        countryy = self.country

    def serialize(self):
        return {
            'street': self.street,
            'street_number': self.street_number,
            'city': self.city,
            'state': self.state,
            'post_code': self.post_code,
            'country': self.country
        }