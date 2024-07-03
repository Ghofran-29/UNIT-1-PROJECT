import json
import re


class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.rented_cars = []

    def add_rented_car(self, car_id):
        self.rented_cars.append(car_id)

    def remove_rented_car(self, car_id):
        self.rented_cars.remove(car_id)

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'rented_cars': self.rented_cars
        }

class CustomerManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.customers = self.load_customers()

    def load_customers(self):
        try:
            with open(self.file_path, 'r') as file:
                customers_data = json.load(file)
                customers = [Customer(
                    customer_id=customer['customer_id'],
                    name=customer['name'],
                    email=customer['email'],
                    phone=customer['phone']
                ) for customer in customers_data]
                for customer, data in zip(customers, customers_data):
                    customer.rented_cars = data.get('rented_cars', [])
                return customers
        except FileNotFoundError:
            print("Initial customers data file not found.")
            return []

    def save_customers(self):
        with open(self.file_path, 'w') as file:
            json.dump([customer.to_dict() for customer in self.customers], file, indent=4)

    def add_customer(self, customer_id, name, email, phone):
        if not self.is_valid_email(email):
            print("Invalid email format. Email should end with @gmail.com.")
            return
        if not self.is_valid_phone(phone):
            print("Invalid phone number format. Phone should start with 05 and be 10 digits long.")
            return

        new_customer = Customer(customer_id, name, email, phone)
        self.customers.append(new_customer)
        self.save_customers()

    def list_customers(self):
        return self.customers

    def get_customer_by_id(self, customer_id):
        return next((customer for customer in self.customers if customer.customer_id == customer_id), None)

    def update_customer(self, customer_id, name, email, phone):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            if not self.is_valid_email(email):
                print("Invalid email format. Email should end with @gmail.com.")
                return
            if not self.is_valid_phone(phone):
                print("Invalid phone number format. Phone should start with 05 and be 10 digits long.")
                return

            customer.name = name
            customer.email = email
            customer.phone = phone
            self.save_customers()

    def delete_customer(self, customer_id):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            self.customers.remove(customer)
            self.save_customers()

    def add_rented_car(self, customer_id, car_id):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.add_rented_car(car_id)
            self.save_customers()

    @staticmethod
    def is_valid_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
        return re.match(regex, email) is not None

    @staticmethod
    def is_valid_phone(phone):
        regex = r'^05[0-9]{8}$'
        return re.match(regex, phone) is not None
