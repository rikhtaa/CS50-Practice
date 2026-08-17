# TUPLES

# A tuple is an immutable sequence.
# Immutable means its values cannot be changed after creation.

numbers = (1, 2, 3)

# numbers[0] = 10
# Raises TypeError because tuples are immutable.


# CLASSES & OBJECTS

# A class is a blueprint for creating objects.
# A class allows us to create our own data type.

class Student:

    # __init__ is called automatically when a new object is created.
    # It initializes the object's data.

    def __init__(self, name, house):

        if not name:
            raise ValueError("Missing name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        # Attributes
        # Store data inside the object.
        self.name = name
        self.house = house

    # __str__ defines what should be returned
    # when the object is converted to a string.

    def __str__(self):
        return "a student"


def main():

    # Creating an object of the Student class.
    student = get_student()

    print(f"{student.name} from {student.house}")


def get_student():

    name = input("Name: ")
    house = input("House: ")

    # Student(...) calls the constructor
    # and creates a Student object.

    return Student(name, house)


main()


# METHODS

# A method is simply a function that belongs to an object/class.

# For example:
#
# student.some_method()
#
# The method can access the object's data through self.


# __init__

# __init__ basically means:
#
# "When a new object is created, initialize its data like this."


# ATTRIBUTES

# Attributes are variables that belong to an object.

person = Student("Rekhta", "Gryffindor")

# person.name
# person.house


# @property

class Person:

    def __init__(self, name, house):
        self.name = name
        self._house = house

    # @property allows us to access a method
    # like an attribute.

    @property
    def username(self):
        return self.name.lower()


person = Person("Rekhta", "Gryffindor")

# Normal method:
# person.username() → "rekhta"

# With @property:
# person.username → "rekhta"


# GETTERS & SETTERS

class Person:

    def __init__(self, name, house):
        self.name = name
        self._house = house

    # Getter
    # Used to get the value of house.

    @property
    def house(self):
        return self._house

    # Setter
    # Used to control what happens when house is changed.

    @house.setter
    def house(self, house):

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self._house = house


person = Person("Rekhta", "Gryffindor")

# Getter
print(person.house)

# Setter
person.house = "Slytherin"


# @classmethod

# @classmethod creates a method that belongs to the class
# rather than a particular object.

class User:

    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)


# We don't need to create an object.
# show_count() works with the class itself.

User.show_count()

# cls refers to the class itself.

# self → current object
# cls  → current class


# INHERITANCE

# Inheritance allows one class to inherit
# attributes and methods from another class.

class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):

        # super() calls the parent class.
        super().__init__(name)

        self.breed = breed


dog = Dog("Buddy", "Labrador")

print(dog.name)
print(dog.breed)