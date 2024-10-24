# Write a Python class that has two methods: get_String and print_String , get_String
# accept a string from the user and print_String prints the string in upper case.

"""
class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def get_string(self):
        self.user_string = input("Enter a string: ")

    def print_string(self):
        print(self.user_string.upper())

if __name__ == "__main__":
    sm = StringManipulator()
    sm.get_string()
    sm.print_string()

"""

# Write a Python program to create a calculator class. Include methods for basic
# arithmetic operations.

"""class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

if __name__ == "__main__":
    calc = Calculator()


    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = calc.add(num1, num2)
                print(f"Result: {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"Result: {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"Result: {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please choose a valid operation.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
"""

# Write a Python class named Circle constructed from a radius and two methods that
# will compute the area and the perimeter of a circle.

"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":

    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)

    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")

"""

# Write a Python class to implement pow(x, n).

"""
def pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        for _ in range(n):
            result *= x
        
        return result

if __name__ == "__main__":
      base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (n): "))
    
power_calculator = pow()
result = power_calculator.pow(base, exponent)
    
print(f"{base} raised to the power of {exponent} is: {result}")

"""

# Write a Python program to create a class representing a shopping cart. Include
# methods for adding and removing items, and calculating the total price.

"""
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} of {name} at ${price:.2f} each.")

    def remove_item(self, name, quantity=1):
        if name in self.items:
            if self.items[name]['quantity'] > quantity:
                self.items[name]['quantity'] -= quantity
                print(f"Removed {quantity} of {name}.")
            elif self.items[name]['quantity'] == quantity:
                del self.items[name]
                print(f"Removed all of {name}.")
            else:
                print(f"Cannot remove {quantity} of {name}, only {self.items[name]['quantity']} in cart.")
        else:
            print(f"{name} is not in the cart.")

    def total_price(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for name, info in self.items.items():
                print(f"{name}: {info['quantity']} @ ${info['price']:.2f} each")

if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Total price")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the shopping cart.")
            break

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            cart.add_item(name, price, quantity)
        
        elif choice == '2':
            name = input("Enter item name to remove: ")
            quantity = int(input("Enter quantity to remove: "))
            cart.remove_item(name, quantity)
        
        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            print(f"Total price: ${cart.total_price():.2f}")

        else:
            print("Invalid option. Please choose a valid operation.")

"""

# Write a Python class Employee with attributes like emp_id, emp_name,
# emp_salary, and emp_department and methods like
# calculate_emp_salary, emp_assign_department, and
# print_employee_details. 
# Sample Employee Data:
# &quot;ADAMS&quot;, &quot;E7876&quot;, 50000, &quot;ACCOUNTING&quot;
# &quot;JONES&quot;, &quot;E7499&quot;, 45000, &quot;RESEARCH&quot;
# &quot;MARTIN&quot;, &quot;E7900&quot;, 50000, &quot;SALES&quot;
# &quot;SMITH&quot;, &quot;E7698&quot;, 55000, &quot;OPERATIONS&quot;
#  Use &#39;assign_department&#39; method to change the department of an
# employee.
#  Use &#39;print_employee_details&#39; method to print the details of an employee.
#  Use &#39;calculate_emp_salary&#39; method takes two arguments: salary and
# hours_worked, which is the number of hours worked by the employee. If
# the number of hours worked is more than 50, the method computes
# overtime and adds it to the salary. Overtime is calculated as following
# formula:
#  overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

"""
class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department
        print(f"{self.emp_name} has been assigned to {new_department}.")

    def calculate_emp_salary(self, hours_worked):
        base_salary = self.emp_salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (base_salary / 50)
            total_salary = base_salary + overtime_amount
        else:
            total_salary = base_salary
        return total_salary

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary:.2f}")
        print(f"Employee Department: {self.emp_department}")

employees = [
    Employee("ADAMS", "E7876", 50000, "ACCOUNTING"),
    Employee("JONES", "E7499", 45000, "RESEARCH"),
    Employee("MARTIN", "E7900", 50000, "SALES"),
    Employee("SMITH", "E7698", 55000, "OPERATIONS"),
]

if __name__ == "__main__":
    for emp in employees:
        emp.print_employee_details()
        print()

    employees[0].assign_department("FINANCE")
    employees[0].print_employee_details()

    hours_worked = 60
    salary = employees[0].calculate_emp_salary(hours_worked)
    print(f"Total Salary for {employees[0].emp_name} for {hours_worked} hours worked: ${salary:.2f}")

"""

# Write a  Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance.

"""
class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}"

if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", "2024-01-01")

    print(account.check_balance())
    account.deposit(500)
    account.withdraw(200)
    print(account.check_balance())
    account.withdraw(400)

"""

# 8. Create a class hierarchy for different types of geometric shapes, including circles,
# rectangles, and triangles, using inheritance.
# Tasks:
# A. Define a base class called Shape with common attributes like colour and area.
# B. Implement subclasses for specific shape types such as Circle, Rectangle,
# and Triangle. Each subclass should inherit from the Shape class.
# C. Incorporate additional attributes and methods specific to each shape type. For
# example, a Circle class might have attributes like radius and methods
# like calculate_area.
# D. Use inheritance to create subclasses representing variations within each shape
# type. For example, within the Rectangle class, create subclasses
# for Square and Parallelogram.
# E. Implement methods or attributes in the subclasses to demonstrate how inheritance
# allows for the sharing of attributes and methods from parent classes.
# F. Create instances of the various shape classes and test their functionality to ensure
# that attributes and methods work as expected.

"""
import math

class Shape:
    def __init__(self, colour):
        self.colour = colour

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__(colour)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius} and colour {self.colour}"

class Rectangle(Shape):
    def __init__(self, width, height, colour):
        super().__init__(colour)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width}, height {self.height}, and colour {self.colour}"

class Square(Rectangle):
    def __init__(self, side_length, colour):
        super().__init__(side_length, side_length, colour)

    def __str__(self):
        return f"Square with side length {self.width} and colour {self.colour}"

class Parallelogram(Rectangle):
    def __init__(self, base, height, colour):
        super().__init__(base, height, colour)

    def __str__(self):
        return f"Parallelogram with base {self.width}, height {self.height}, and colour {self.colour}"

class Triangle(Shape):
    def __init__(self, base, height, colour):
        super().__init__(colour)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle with base {self.base}, height {self.height}, and colour {self.colour}"

if __name__ == "__main__":
    circle = Circle(radius=5, colour="red")
    rectangle = Rectangle(width=4, height=6, colour="blue")
    square = Square(side_length=3, colour="green")
    parallelogram = Parallelogram(base=5, height=4, colour="yellow")
    triangle = Triangle(base=4, height=3, colour="purple")

    shapes = [circle, rectangle, square, parallelogram, triangle]
    
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area():.2f}\n")
        
"""

# Create a Bus child class that inherits from the Vehicle class. The default fare charge of
# any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an
# extra 10% on full fare as a maintenance charge. So total fare for bus instance will
# become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5550.
# You need to override the fare() method of a Vehicle class in Bus class.

"""
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self):
        super().__init__(seating_capacity=50)

    def fare(self):
        base_fare = super().fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

if __name__ == "__main__":
    bus = Bus()
    print(f"The total fare for the bus is: ${bus.fare():.2f}")

    """