#1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_name(self):
        print(f'Maximum speed - {self.max_speed}, mileage - {self.mileage}')


vehicle = Vehicle(90, 7000)
vehicle.print_name()

#2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):

    def __init__(self, max_speed, mileage, seating_capacity):
        self.seating_capacity = seating_capacity
        super(Bus, self).__init__(max_speed, mileage)

    def seat_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def number_of_seats(self):
        print(f'Bus capacity: {self.seating_capacity}')


bus = Bus(120, 16000, 1)
bus.print_name()
bus.number_of_seats()

#3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(bus))

print(issubclass(Bus, Vehicle))

#4. Determine if School_bus is also an instance of the Vehicle class

print(isinstance(bus, Vehicle))

#5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_id(self):
        print(f'School id - {self.get_school_id}, students number - {self.number_of_students}')


school = School(15, 999)
school.school_id()

#6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):

    def __init__(self, school_id, max_speed, mileage, seating_capacity, bus_school_color, number_of_students):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def color_bus(self):
        print(f'Bus color - {self.bus_school_color}')


school_bus = SchoolBus(15, 999, 150,9000, 'Red', 5)
school_bus.color_bus()

print(isinstance(bus, Vehicle))

#7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
#make a tuple of it and by using for call their action using the same method.
#Magic methods:

class Beer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound (self):
        print('ar')

class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound (self):
        print('auu')

bear = Beer('Grizli', 7)
wolf = Wolf('Grey', 3)

for animal in (bear, wolf):
    animal.make_sound()

#8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
#otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    def __str__(self):
        return f'City {self.name} - {self.population} people'

people = City('Lviv', 1000000)
print(people)
people_2 = City('Zolochiv', 900)
print(people_2)

#9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'

people = City('Lviv', 1000000)
print(people)
people_2 = City('Zolochiv', 900)
print(people_2)

#10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

class Count:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 or other.count > 10:
            total_count = self.count * other.count
        else:
            total_count = self.count + other.count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'

a1 = Count(8)
a2 = Count(9)
a3 = a1 + a2
print(a3)

#11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
#Create a new class with __call__ method and define this call to return sum.

class Call:

    def __call__(self, * args):
        return sum(args)

area = Call()
print(area(5, 9, 5, 15, 37))

#12*. Making Your Objects Truthy or Falsey Using __bool__().
#Create class MyOrder with cart and customer instance attributes.
#Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
#e.g.:
#order_1 = MyOrder(['a', 'b', 'c'], 'd')
#order_2 = MyOrder([], 'a')
#bool(order_1)
#True
#bool(order_2)
#False

class MyOrder:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))