from car import CarManager
from customer import CustomerManager
from rental import RentalManager
from datetime import datetime
from colorama import init, Fore

# Initialize colorama
init()

def load_initial_data():
    car_manager = CarManager('data/cars.json')
    customer_manager = CustomerManager('data/customers.json')
    rental_manager = RentalManager('data/rentals.json')

    rental_manager.set_car_manager(car_manager)
    rental_manager.set_customer_manager(customer_manager)

    return car_manager, customer_manager, rental_manager

def main_menu():
    while True:
        print(Fore.LIGHTRED_EX +"\nMain Menu:"+Fore.RESET)
        print("1. Manage cars")
        print("2. Manage customers")
        print("3. Manage rentals")
        print("4. Reports and Statistics")
        print("5. Exit")
        choice = input(Fore.LIGHTCYAN_EX + "Enter a choice from 1 to 4:" + Fore.RESET)
        if choice == '1':
            manage_cars_menu(car_manager)
        elif choice == '2':
            manage_customers_menu(customer_manager)
        elif choice == '3':
            manage_rentals_menu(car_manager, customer_manager, rental_manager)
        elif choice == '4':
            report_menu(car_manager, rental_manager)
        elif choice == '5':
            break
        else:
            print(Fore.LIGHTRED_EX+"Invalid choice. Please enter a number from 1 to 5."+Fore.RESET)

def manage_cars_menu(car_manager):
    while True:
        print(Fore.LIGHTRED_EX + "\nManage Cars Menu:" + Fore.RESET)
        print("1. Add a car")
        print("2. List available cars")
        print("3. Update a car")
        print("4. Delete a car")
        print("5. Back to Main Menu")
        choice = input(Fore.LIGHTYELLOW_EX+"Enter your choice: "+Fore.RESET)
        if choice == '1':
            car_id = input("Enter car ID: ")
            brand = input("Enter car brand: ")
            model = input("Enter car model: ")
            price = float(input("Enter car price per day: "))
            car_manager.add_car(car_id, brand, model, price)
            print(Fore.LIGHTBLUE_EX+"Car added successfully."+Fore.RESET)
        elif choice == '2':
            available_cars = car_manager.list_available_cars()
            if available_cars:
                for car in available_cars:
                    print(f"Car ID: {car.car_id}, Brand: {car.brand}, Model: {car.model}, Price: {car.price}, Availability: {car.availability}")
            else:
                print("No available cars.")
        elif choice == '3':
            car_id = input("Enter car ID to update : ")
            price = float(input("Enter new price per day (leave blank to keep current):: "))
            availability = input("Enter new availability (True/False) (leave blank to keep current): ").lower() == 'true'
            car_manager.update_car(car_id, price, availability)
            print(Fore.LIGHTBLUE_EX+"Car updated successfully."+Fore.RESET)

        elif choice == '4':
            car_id = input("Enter car ID to delete: ")
            car_manager.delete_car(car_id)
            print(Fore.LIGHTBLUE_EX+"Car deleted successfully."+Fore.RESET)
        elif choice == '5':
            break
        else:
            print(Fore.LIGHTRED_EX+"Invalid choice. Please enter a number from 1 to 5."+Fore.RESET)

def manage_customers_menu(customer_manager):
    while True:
        print(Fore.LIGHTRED_EX + "\nManage Customers Menu:" +Fore.RESET)
        print("1. Add a new customer")
        print("2. List customers")
        print("3. Show customer details")
        print("4. Update a customer")
        print("5. Delete a customer")
        print("6. Back to Main Menu")
        choice = input(Fore.LIGHTYELLOW_EX+"Enter your choice: "+Fore.RESET)
        if choice == '1':
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            email = input("Enter customer email (must end with @gmail.com): ")
            phone = input("Enter customer phone number (must start with 05 and be 10 digits long): ")
            customer_manager.add_customer(customer_id, name, email, phone)
            print(Fore.LIGHTBLUE_EX+"Customer added successfully."+Fore.RESET)
        elif choice == '2':
            customers = customer_manager.list_customers()
            for customer in customers:
                print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")
        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            customer = customer_manager.get_customer_by_id(customer_id)
            if customer:
                print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}, Rented Cars: {customer.rented_cars}")
            else:
                print(Fore.LIGHTGREEN_EX+"Customer not found."+Fore.RESET)
        elif choice == '4':
            customer_id = input("Enter customer ID: ")
            name = input("Enter new customer name: ")
            email = input("Enter new customer email (must end with @gmail.com): ")
            phone = input("Enter new customer phone number (must start with 05 and be 10 digits long): ")
            customer_manager.update_customer(customer_id, name, email, phone)
            print(Fore.LIGHTBLUE_EX + "Customer updated successfully." + Fore.RESET)
        elif choice == '5':
            customer_id = input("Enter customer ID: ")
            customer_manager.delete_customer(customer_id)
            print(Fore.LIGHTBLUE_EX + "Customer deleted successfully." + Fore.RESET)
        elif choice == '6':
            break
        else:
            print(Fore.RED +"Invalid choice. Please enter a number from 1 to 6."+Fore.RESET)


def manage_rentals_menu(car_manager, customer_manager, rental_manager):
    while True:
        print(Fore.LIGHTRED_EX + "\nManage Rentals Menu:" + Fore.RESET)
        print("1. Rent a car")
        print("2. Return a car")
        print("3. List rented cars")
        print("4. List returned cars")
        print("5. Back to Main Menu")
        choice = input(Fore.LIGHTYELLOW_EX +"Enter your choice: "+Fore.RESET)
        if choice == '1':
            car_id = input("Enter car ID: ")
            customer_id = input("Enter customer ID: ")
            rent_date = datetime.now()
            rental_manager.rent_car(car_id, customer_id, rent_date)
            car_manager.update_car_availability(car_id, False)
            customer_manager.add_rented_car(customer_id, car_id)
            print(Fore.LIGHTBLUE_EX + "Car rented successfully." + Fore.RESET)
        elif choice == '2':
            rental_id = int(input("Enter rental ID: "))
            return_date = datetime.now()
            rental_manager.return_car(rental_id, return_date)
            rental = next((r for r in rental_manager.rentals if r.rental_id == rental_id), None)
            if rental:
                car_manager.update_car_availability(rental.car_id, True)
                print(Fore.LIGHTBLUE_EX + "Car return successfully." + Fore.RESET)
        elif choice == '3':
            rented_cars = rental_manager.list_rented_cars()
            for rental in rented_cars:
                car = car_manager.get_car_by_id(rental.car_id)
                customer = customer_manager.get_customer_by_id(rental.customer_id)
                if car and customer:
                    print(
                        f"Rental ID: {rental.rental_id}, Car: {car.brand} {car.model}, Customer: {customer.name}, Rent Date: {rental.rent_date}, Return Date: {rental.return_date}")
                else:
                    print(
                        f"Rental ID: {rental.rental_id}, Car ID: {rental.car_id}, Customer ID: {rental.customer_id}, Rent Date: {rental.rent_date}, Return Date: {rental.return_date} (Details missing)")
        elif choice == '4':
            returned_cars = rental_manager.list_returned_cars()
            for rental in returned_cars:
                car = car_manager.get_car_by_id(rental.car_id)
                customer = customer_manager.get_customer_by_id(rental.customer_id)
                if car and customer:
                    print(
                        f"Rental ID: {rental.rental_id}, Car: {car.brand} {car.model}, Customer: {customer.name}, Rent Date: {rental.rent_date}, Return Date: {rental.return_date}")
                else:
                    print(
                        f"Rental ID: {rental.rental_id}, Car ID: {rental.car_id}, Customer ID: {rental.customer_id}, Rent Date: {rental.rent_date}, Return Date: {rental.return_date} (Details missing)")
        elif choice == '5':
            break
        else:
            print(Fore.LIGHTRED_EX + "Invalid choice. Please enter a number from 1 to 5." +Fore.RESET)
def report_menu(car_manager, rental_manager):
    while True:
        print(Fore.LIGHTRED_EX +  "\nReports and Statistics Menu:" +Fore.RESET)
        print("1. Generate most rented cars report")
        print("2. Generate complete report of all rentals")
        print("3. Back to Main Menu")
        choice = input(Fore.LIGHTYELLOW_EX +"Enter your choice: "+Fore.RESET)

        if choice == '1':
            generate_most_rented_cars_report(car_manager, rental_manager)
        elif choice == '2':
            generate_complete_report(rental_manager)
        elif choice == '3':
            break
        else:
            print(Fore.RED+"Invalid choice. Please enter a number from 1 to 3."+Fore.RESET)

def generate_most_rented_cars_report(car_manager, rental_manager):
    rental_manager.generate_most_rented_cars_report()

def generate_complete_report(rental_manager):
    rental_manager.generate_complete_report()

if __name__ == "__main__":
    car_manager, customer_manager, rental_manager = load_initial_data()
    main_menu()
