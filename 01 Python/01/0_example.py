print("Hello World!")

age = input("How old are you?")
print("You are: " + age + " years old!")

def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python script example.")

def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")

def main():
    name = input("What is your name?\n")
    greet_user(name)

    try:
        number = float(input("Enter a number to check if it is positive, zero, or negative:\n"))
        check_number(number)
    except ValueError:
        print("That's not a valid number.")

    print("Let's print numbers from 1 to 5:")
    for i in range(1, 6):
        print(i)

if __name__ == "__main__":
    main()
