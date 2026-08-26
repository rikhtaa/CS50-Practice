# Sets
# A set is a data type like a list, but it does not allow duplicate values.

# Global Variables
# To modify a global variable inside a function, use the global keyword.

balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()


# Constants
# Constants are typically written using capital letters
# and are placed near the top of the code.

MAX_BALANCE = 10000


# Type Hints
# Type hints specify the expected types of function arguments and return values.
# Tools like mypy can use type hints to check your code without running it.

def add(a: int, b: int) -> int:
    return a + b


result = add(5, 10)
print(result)


# Docstrings
# A docstring documents what a function, class, or module does.

def square(n):
    """Return the square of n."""
    return n * n


print(square(5))


# argparse
# argparse allows a program to accept arguments from the command line.
#
# Example:
# python hello.py Rekhta
#
# Output:
# Hello, Rekhta!
#
# You can also use:
# python hello.py --help

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")

args = parser.parse_args()

print(f"Hello, {args.name}!")


# Unpacking with *
# * unpacks a list or tuple into separate positional arguments.
#
# total(*coins) is equivalent to:
#
# total(100, 50, 25)

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")


# *args and **kwargs
#
# *args collects multiple positional arguments into a tuple.
# **kwargs collects multiple keyword arguments into a dictionary.

def test(*args, **kwargs):
    print(args)
    print(kwargs)


test(10, 20, name="Rekhta")


# map()
# map() applies a function to every item in a collection.
#
# Python's map() returns an iterator.
# Use list() if you want the results as a list.

numbers = [1, 2, 3, 4]

squares = map(lambda x: x * x, numbers)

print(list(squares))


# List Comprehensions
# A list comprehension is a short way to create a new list
# by performing an operation on each item.

numbers = [1, 2, 3, 4]

squares = [number * number for number in numbers]

print(squares)


# filter()
# filter() keeps the items for which the condition is True.
#
# Python's filter() returns an iterator.

numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)

print(list(even))


# Dictionary Comprehensions
# A dictionary comprehension is a short way to create a new dictionary.

numbers = [1, 2, 3, 4]

squares = {x: x * x for x in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16}


# enumerate()
# enumerate() gives you both the item and its index while looping.

names = ["Harry", "Ron", "Hermione"]

for i, name in enumerate(names):
    print(i, name)

# Output:
# 0 Harry
# 1 Ron
# 2 Hermione


# Iterators
# An iterator is something that gives you one item at a time.

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# Output:
# 10
# 20
# 30


# Generators
# A generator is a convenient way to create an iterator.
# Generators use the yield keyword.

def numbers_generator():
    yield 1
    yield 2
    yield 3


for number in numbers_generator():
    print(number)

# Output:
# 1
# 2
# 3


# yield
# yield gives a value and pauses the function.
# The function continues from where it stopped
# when the next value is requested.