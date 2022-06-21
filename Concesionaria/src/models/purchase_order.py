import uuid

def purchase_number_generator():

    return uuid.uuid4()

class Purchase_order:

    def __init__(self, id, purchase_number, amount, car_model):
        self.id = id
        self.purchase_number = purchase_number
        self.amount = amount
        self.car_model = car_model

    def serialize(self):
        return {
            "id": self.id,
            "purchase_number": self.purchase_number,
            "amount": self.amount,
            "car_model": self.car_model
        }
