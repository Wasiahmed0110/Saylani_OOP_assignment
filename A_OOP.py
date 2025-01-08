# 1. Person class
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Country: {self.country}")

person1 = Person("Alice", 30, "USA")
person2 = Person("Bob", 25, "UK")
person1.display_details()
person2.display_details()

# 2. Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

# 3. Vehicle and Car classes
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_details(self):
        super().display_details()
        print(f"Doors: {self.doors}")

car = Car("Toyota", "Corolla", 2022, 4)
car.display_details()

# 4. BankAccount class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Account Balance: {account.balance}")

# 5. Shape, Circle, and Triangle classes
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(7)
triangle = Triangle(10, 5)
print(f"Circle Area: {circle.area()}, Triangle Area: {triangle.area()}")

# 6. Employee and Manager classes
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, department, bonus):
        super().__init__(name, salary)
        self.department = department
        self.bonus = bonus

    def annual_salary(self):
        return super().annual_salary() + self.bonus

manager1 = Manager("Anna", 5000, "HR", 2000)
manager2 = Manager("John", 6000, "IT", 3000)
print(f"Manager 1 Annual Salary: {manager1.annual_salary()}")
print(f"Manager 2 Annual Salary: {manager2.annual_salary()}")

# 7. Book and Ebook classes
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}")

class Ebook(Book):
    def __init__(self, title, author, publication_year, price):
        super().__init__(title, author, publication_year)
        self.price = price

    def display_details(self):
        super().display_details()
        print(f"Price: ${self.price}")

ebook = Ebook("Python 101", "John Doe", 2021, 29.99)
ebook.display_details()

# 8. Animal and Dog classes
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} goes '{self.sound}'")

class Dog(Animal):
    def __init__(self, species, sound, color):
        super().__init__(species, sound)
        self.color = color

    def make_sound(self):
        print(f"The {self.color} {self.species} goes '{self.sound}'")

dog = Dog("dog", "woof", "brown")
dog.make_sound()

# 9. Bank class
class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def remove_branch(self, branch):
        self.branches.remove(branch)

    def display_branches(self):
        print(f"Bank: {self.name}, Branches: {', '.join(self.branches)}")

bank = Bank("National Bank")
bank.add_branch("Downtown")
bank.add_branch("Uptown")
bank.remove_branch("Uptown")
bank.display_branches()

# 10. Product and PersonalCareProduct classes
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity

class PersonalCareProduct(Product):
    def __init__(self, product_id, name, price, warranty):
        super().__init__(product_id, name, price)
        self.warranty = warranty

    def total_price(self, quantity):
        return super().total_price(quantity)  # Include logic for warranty if needed

product = PersonalCareProduct(1, "Shampoo", 10, "1 year")
print(f"Total Price: ${product.total_price(3)}")

# 11. Enhanced BankAccount with transfer
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount

account1 = BankAccount("111", "Alice", 1000)
account2 = BankAccount("222", "Bob", 500)
account1.transfer(200, account2)
print(f"Alice's Balance: {account1.balance}, Bob's Balance: {account2.balance}")

# 12. University class
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def remove_department(self, department):
        self.departments.remove(department)

    def display_departments(self):
        print(f"University: {self.name}, Departments: {', '.join(self.departments)}")

university = University("Tech University")
university.add_department("Computer Science")
university.add_department("Physics")
university.remove_department("Physics")
university.display_departments()
