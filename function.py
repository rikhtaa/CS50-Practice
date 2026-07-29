# function
def hello():
 return "hello"

# variable
# name = input("What's your name? ")
# print(name)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main() 