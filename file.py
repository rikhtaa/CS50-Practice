import csv

# File I/O is the ability of a program to take a file as input
# or create a file as output.

# open() is a built-in Python function that allows you to open a file
# and use it in your program. You can open a file to read from it
# or write to it.

# with automatically opens and closes the file.

# WRITE

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


# READ

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "home": row["home"]
        })

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# CSV file extension: .csv


# Anonymous function:
# lambda is used to create a small anonymous function.


# PIL (Python Imaging Library)
