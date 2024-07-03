import json
from datetime import datetime

class Rental:
    def __init__(self, rental_id, car_id, customer_id, rent_date, return_date=None):
        self.rental_id = rental_id
        self.car_id = car_id
        self.customer_id = customer_id
        self.rent_date = rent_date
        self.return_date = return_date

    def to_dict(self):
        return {
            'rental_id': self.rental_id,
            'car_id': self.car_id,
            'customer_id': self.customer_id,
            'rent_date': self.rent_date.isoformat(),
            'return_date': self.return_date.isoformat() if self.return_date else None
        }

class RentalManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.rentals = self.load_rentals()
        self.car_manager = None
        self.customer_manager = None

    def set_car_manager(self, car_manager):
        self.car_manager = car_manager

    def set_customer_manager(self, customer_manager):
        self.customer_manager = customer_manager

    def load_rentals(self):
        try:
            with open(self.file_path, 'r') as file:
                rentals_data = json.load(file)
                rentals = [Rental(
                    rental_id=rental['rental_id'],
                    car_id=rental['car_id'],
                    customer_id=rental['customer_id'],
                    rent_date=datetime.fromisoformat(rental['rent_date']),
                    return_date=datetime.fromisoformat(rental['return_date']) if rental['return_date'] else None
                ) for rental in rentals_data]
                return rentals
        except FileNotFoundError:
            print("Initial rentals data file not found.")
            return []

    def save_rentals(self):
        with open(self.file_path, 'w') as file:
            json.dump([rental.to_dict() for rental in self.rentals], file, indent=4)

    def rent_car(self, car_id, customer_id, rent_date):
        rental_id = len(self.rentals) + 1
        new_rental = Rental(rental_id, car_id, customer_id, rent_date)
        self.rentals.append(new_rental)
        self.save_rentals()

    def return_car(self, rental_id, return_date):
        rental = next((rental for rental in self.rentals if rental.rental_id == rental_id), None)
        if rental:
            rental.return_date = return_date
            self.save_rentals()



    def list_rented_cars(self):
        return [rental for rental in self.rentals if rental.return_date is None]

    def list_returned_cars(self):
        return [rental for rental in self.rentals if rental.return_date is not None]

    def generate_daily_revenue_report(self, date_str):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        daily_revenue = 0
        for rental in self.rentals:
            if rental.rent_date.date() == date.date() or (rental.return_date and rental.return_date.date() == date.date()):
                car = self.car_manager.get_car_by_id(rental.car_id)
                days_rented = (rental.return_date - rental.rent_date).days if rental.return_date else (date - rental.rent_date).days
                daily_revenue += car.price * days_rented
        print(f"Total revenue for {date_str}: {daily_revenue}")



    def generate_most_rented_cars_report(self):
        car_rental_count = {}
        for rental in self.rentals:
            car_rental_count[rental.car_id] = car_rental_count.get(rental.car_id, 0) + 1
        most_rented_cars = sorted(car_rental_count.items(), key=lambda x: x[1], reverse=True)
        print("Most rented cars:")
        for car_id, count in most_rented_cars:
            car = self.car_manager.get_car_by_id(car_id)
            print(f"Car ID: {car_id}, Brand: {car.brand}, Model: {car.model}, Times Rented: {count}")

    def generate_complete_report(self):
        for rental in self.rentals:
            car = self.car_manager.get_car_by_id(rental.car_id)
            customer = self.customer_manager.get_customer_by_id(rental.customer_id)
            print(f"Rental ID: {rental.rental_id}, Car: {car.brand} {car.model}, Customer: {customer.name}, Rent Date: {rental.rent_date}, Return Date: {rental.return_date}")
