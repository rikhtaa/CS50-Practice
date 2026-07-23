import requests
import random
import cowsay
import sys
import json


# random module

# random.choice()  returns a random item from a list
coin = random.choice(["heads", "tails"])

# random.randint()  returns a random integer between two values
number = random.randint(1, 10)

print(coin, number)


# random.shuffle()  shuffles a list in place
cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)


# packages

# third party libraries can be installed for extra functionality
# pip is the package manager used to install packages

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])


# sys module

# sys.argv  stores command-line arguments
# sys.exit()  exits the program

if len(sys.argv) != 2:
    sys.exit()


# APIs

# requests.get()  sends a GET request to an API
# res.json()  converts JSON response into a Python dictionary
# json.dumps()  prints JSON in a readable format

res = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)

print(json.dumps(res.json(), indent=2))