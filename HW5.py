# 1.
# class Laptop:
#    """
#    Make the class with composition.
#    """
# class Battery:
#    """
#    Make the class with composition.
#    """
class Laptop:
    def __init__(self, laptop_name, laptop_model, battery_model, battery_type, battery_capacity):
        self.laptop_name = laptop_name
        self.laptop_model = laptop_model

        self.laptop_battery = Battery(battery_model, battery_type, battery_capacity)

    def __str__(self):
        return f'{self.laptop_name} {self.laptop_model} with battery {self.laptop_battery}'


class Battery:
    def __init__(self, battery_model, battery_type, battery_capacity):
        self.battery_model = battery_model
        self.battery_type = battery_type
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f'{self.battery_model} {self.battery_type} {self.battery_capacity}'


dell_laptop = Laptop('DELL', 'Latitude E7450', '1234', 'Li-ion', '14')
print(dell_laptop)


# 2.
# class Guitar:
#    """
#    Make the class with aggregation
#    """
# class GuitarString:
#    """
#    Make the class with aggregation
#    """
class Guitar:
    def __init__(self, guitar_model):
        self.guitar_model = guitar_model

    def __str__(self):
        return f'{self.guitar_model}'


class GuitarStrings:
    def __init__(self, guitar_model, number_of_strings):
        self.guitar_model = guitar_model
        self.number_of_strings = number_of_strings

    def __str__(self):
        return f'{self.guitar_model} - {self.number_of_strings} strings'


guitar = Guitar('Gibson Firebird')
guiter_strings = GuitarStrings(guitar, '6')
print(guiter_strings)


# 3
# class Calc:
#    """
#    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#    Note: this method should not take instance as first parameter.
#    """

class Calc:
    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3


summa = Calc.add_nums(3, 4, 5)
print(summa)


# 4*.
# class Pasta:
#    """
#    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#    It should have 2 methods:
#    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#    which should create Pasta instances with predefined list of ingredients.
#    Example:
#        pasta_1 = Pasta(["tomato", "cucumber"])
#        pasta_1.ingredients will equal to ["tomato", "cucumber"]
#        pasta_2 = Pasta.bolognaise()
#        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#    """

class Pasta:
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['tomato', 'cucumber'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(f'pasta_1.ingredients will equal to {pasta_1.list_of_ingredients}')
pasta_2 = Pasta.bolognaise()
print(f'pasta_2.ingredients will equal to {pasta_2.list_of_ingredients}')


# 5*.
# class Concert:
#    """
#    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#    In case of setting visitors_count - max_visitors_num should be checked,
#    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#    Example:
#        Concert.max_visitor_num = 50
#        concert = Concert()
#        concert.visitors_count = 1000
#        print(concert.visitors_count)  # 50
#    """
class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


concert = Concert()
Concert.max_visitors_num = 50
concert.visitors_count = 1000
print(concert.visitors_count)

# 6.
# class AddressBookDataClass:
#    """
#    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#    """

import dataclasses


@dataclasses.dataclass()
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


note_book = AddressBookDataClass(1, 'Taras', '0968090269', 'city.Lviv', 'taras.pohorilets@gmail.com', '1989', 32)
print(note_book)

# 7. Create the same class (6) but using NamedTuple

import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass',
                                              ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

note_book2 = AddressBookDataClass(1, 'Taras', '0968090269', 'city.Lviv', 'taras.pohorilets@gmail.com', '1989', 32)
print(note_book2)


# 8.
# class AddressBook:
#    """
#    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#    Make its str() representation the same as for AddressBookDataClass defined above.
#    """

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number},' \
               f' address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


address = AddressBook(1, 'Taras', '0968090269', 'city.Lviv', 'taras.pohorilets@gmail.com', '1989', 32)
print(address)


# 9.
# class Person:
#    """
#    Change the value of the age property of the person object
#    """
#    name = "John"
#    age = 36
#    country = "USA"

class Person:
    name = "John"
    age = 36
    country = "USA"


person = Person()
print(person.age)
Person.age = 32
print(person.age)


# 10.
# class Student:
#    """
#    Add an 'email' attribute of the object student and set its value
#    Assign the new attribute to 'student_email' variable and print it by using getattr
#    """
#    id = 0
#    name = ""

#   def __init__(self, id, name):
#        self.id = id
#        self.name = name

class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, 'Taras')
student.email = 'taras.pohorilets@gmail.com'
student_email = getattr(student, 'email')
print(student_email)


# 11*.
# class Celsius:
#    """
#    By using @property convert the celsius to fahrenheit
#    Hint: (temperature * 1.8) + 32)
#    """
#    def __init__(self, temperature=0):
#       self._temperature = temperature

# create an object
# {obj} = ...

# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return self._temperature * 1.8 + 32


obj = Celsius(2)

print(f'{obj.fahrenheit} - Fahrenheit')
