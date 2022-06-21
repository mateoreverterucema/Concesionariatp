
class Specs_autos:

    def __init__(self, id, model, price, body, transmission, power, fuel, top_speed, acceleration_0_100kmh, motor):
        self.id = id
        self.model = model
        self.price = price
        self.body = body
        self.transmission = transmission
        self.power = power
        self.fuel = fuel
        self.top_speed = top_speed
        self.acceleration_0_100kmh = acceleration_0_100kmh
        self.motor: Motor = motor

    def serialize(self):
        return {
            "model": self.model,
            "price": self.price,
            "body": self.body,
            "transmission": self.transmission,
            "power": self.power,
            "fuel": self.fuel,
            "top_speed": self.top_speed,
            "acceleration_0_100kmh": self.acceleration_0_100kmh,
            "motor": self.motor.serialize()
        }

class Motor:

    def __init__(self, cylinders, valves_per_cylinder, turbo, fuel_tank_capacity):
        self.cylinders = cylinders
        self.valves_per_cylinder = valves_per_cylinder
        self.turbo = turbo
        self.fuel_tank_capacity = fuel_tank_capacity

    def serialize(self):
        return {
            "cylinders": self.cylinders,
            "valves_per_cylinder": self.valves_per_cylinder,
            "turbo": self.turbo,
            "fuel_tank_capacity": self.fuel_tank_capacity
        }


class SUV(Specs_autos):
    pass


class Convertible(Specs_autos):
    pass


class Coupe(Specs_autos):
    pass


class Hatchback(Specs_autos):
    pass


class Sedan(Specs_autos):
    pass


class Pick_up(Specs_autos):
    pass