# try code that might raise an exception
# except  runs if the specified exception occurs
# else  runs only if no exception occurs

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# pass  placeholder that does nothing

if user_is_admin:
    pass  # I'll add this later
else:
    print("Access denied")


# common exceptions

# ValueError  invalid value for a function e.g. int("abc")
# ZeroDivisionError  division by zero
# KeyError  accessing a dictionary key that doesn't exist
# EOFError  raised when input() receives end-of-file Ctrl+D 