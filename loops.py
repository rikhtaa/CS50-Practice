# while loop runs until the condition is false
i = 3
while i != 0:
    print("meow")
    i = i - 1


# for loop is useful for iteration of block of code
for i in [0, 1, 2]:
  print("meow")


# dictionary

person = dict(name="Rekhta", age=20)
print(person)
# Output: {'name': 'Rekhta', 'age': 20}


pairs = [("a", 1), ("b", 2)]
d = dict(pairs)

print(d)
# Output: {'a': 1, 'b': 2}


# convert a string into a list of characters

letters = list("hello")
print(letters)
# Output: ['h', 'e', 'l', 'l', 'o']


# useful loop keywords

# break -> exits the loop completely
# continue -> skips the current iteration and starts the next one
# pass -> placeholder that does nothing


# useful list methods

# append() -> adds one item to the end of a list
# extend() -> adds all items from another iterable
# sum() -> returns the sum of all numbers in a list