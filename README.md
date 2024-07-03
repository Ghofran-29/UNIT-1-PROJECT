# UNIT-1-PROJECT



## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)

## Example Project :  An online Grocery Store :

#### Overview : An online store that sells fruits to customers. This online store has 2 main users. The customer and the manager of the store . Each one of them should be able to do the following tasks for the store to function properly . 

#### As a customer I should be able to do the following :
- Browse  Products . 
- View the product info (summary, specs, price, quantity , etc.)
- Search for Products.
- Get recommendations for my next purchase based on my purchase history.
- Add Products to the shopping cart .
- Remove a product from the shopping cart.
- List the products in my shopping cart. 
- Continue to checkout . 
- Fill in my address for delivery.
- Get receipt of my purchases.
- Check delivery status . 



#### Usage :
 Explain to the user how to use your project . 
 for example:
 - type in search product_name to search for a product.
 - type in list_products to show all the products in the grocery.
 - type in show product_name to get information about this product.
 - type in buy product_name to buy the product . 
 - and so on...


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

# Car Rental Store

## Overview
The Car Rental Store is a comprehensive CLI-based application built with Python that allows users to manage car rentals, customer information, and generate various rental-related reports. The project leverages Object-Oriented Programming (OOP) principles to provide a modular and scalable solution.

## User Stories
- **As a customer,** I want to view available cars so that I can choose a car to rent.
- **As a customer,** I want to rent a car by providing my information and the car ID.
- **As a customer,** I want to return a rented car so that I can complete my rental period.
- **As an admin,** I want to add new cars to the inventory so that I can expand the rental fleet.
- **As an admin,** I want to update car details to keep the information current.
- **As an admin,** I want to delete cars that are no longer available for rent.
- **As an admin,** I want to view detailed rental reports to monitor business performance.
- **As an admin,** I want to manage customer information including adding, updating, and deleting customer records.

## Prerequisites
- Python 3.8 or higher
- Required libraries (can be installed via pip):
  - `colorama`

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/car_rental_store.git
   cd car_rental_store
   ```
2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the application:**
   ```bash
   python main.py
   ```
2. **Main Menu Options:**
   - `1. Car Management`:
     - Add, list, show details, update, or delete cars.
   - `2. Rental Operations`:
     - Rent a car, return a rented car, list all rentals, list rented cars, list returned cars.
   - `3. Customer Management`:
     - Add, list, show details, update, or delete customers.
   - `4. Reports and Statistics`:
     - Generate daily, monthly, yearly revenue reports, and most rented cars report.
   - `5. Exit`: Exit the application.

### Car Management Menu
- **Add a new car**: Enter car details such as ID, brand, model, and price.
- **List available cars**: View all cars that are available for rent.
- **Show car details**: Get detailed information about a specific car.
- **Update car information**: Modify car details.
- **Delete a car**: Remove a car from the inventory.

### Rental Operations Menu
- **Rent a car**: Enter car ID, customer ID, and rent date to rent a car.
- **Return a rented car**: Enter rental ID and return date to complete the rental.
- **List all rentals**: View all rental transactions.
- **List rented cars**: View cars that are currently rented out.
- **List returned cars**: View cars that have been returned.

### Customer Management Menu
- **Add a new customer**: Enter customer details such as ID, name, email, and phone number.
- **List registered customers**: View all customers.
- **Show customer details**: Get detailed information about a specific customer.
- **Update a customer**: Modify customer details.
- **Delete a customer**: Remove a customer from the records.

### Reports and Statistics Menu
- **Daily Revenue Report**: Generate a report for the daily revenue.
- **Monthly Revenue Report**: Generate a report for the monthly revenue.
- **Yearly Revenue Report**: Generate a report for the yearly revenue.
- **Most Rented Cars Report**: Generate a report for the most rented cars.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Create a pull request describing your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For support or further information, you can reach out via:
- Email: ghofranalsanosi@gmail.com
- GitHub: [Ghufran](https://github.com/ghufran)

## Additional Notes
- Ensure your email follows the format `name@gmail.com`.
- Phone numbers should be 10 digits long starting with `05`.
- When running the application, enter numbers from 1 to 5 for the menu options to navigate through the system.
