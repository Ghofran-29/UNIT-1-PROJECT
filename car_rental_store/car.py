import json

class Car:
    def __init__(self, car_id, brand, model, price, availability):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.availability = availability

    def to_dict(self):
        return {
            'car_id': self.car_id,
            'brand': self.brand,
            'model': self.model,
            'price': self.price,
            'availability': self.availability
        }

class CarManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cars = self.load_cars()

    def load_cars(self):
        try:
            with open(self.file_path, 'r') as file:
                cars_data = json.load(file)
                cars = [Car(**car) for car in cars_data]
                return cars
        except FileNotFoundError:
            print("Initial cars data file not found.")
            return []

    def save_cars(self):
        with open(self.file_path, 'w') as file:
            json.dump([car.to_dict() for car in self.cars], file, indent=4)

    def add_car(self, car_id, brand, model, price, availability=True):
        new_car = Car(car_id, brand, model, price, availability)
        self.cars.append(new_car)
        self.save_cars()

    def list_available_cars(self):
        return [car for car in self.cars if car.availability]

    def get_car_by_id(self, car_id):
        return next((car for car in self.cars if car.car_id == car_id), None)

    def update_car(self, car_id, price, availability):
        car = self.get_car_by_id(car_id)
        if car:
            if price:
                car.price = price
            if availability:
                car.availability = availability
            self.save_cars()

    def delete_car(self, car_id):
        self.cars = [car for car in self.cars if car.car_id != car_id]
        self.save_cars()

    def update_car_availability(self, car_id, availability):
        car = self.get_car_by_id(car_id)
        if car:
            car.availability = availability
            self.save_cars()
