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
""