import math

def greet_user():
    #Asks for user input
    user = input('Enter your name: ')
    print("Hello " + user + "!")

def circle_area():
    #Asks user to enter radius
    radius = float(input('Enter a radius: '))
    area = math.pi * radius ** 2
    print("The area is: " + str(area))

def rectangle_height():
    pass
def add_values():
    pass
def mass_converter():
    pass
def random_generator():
    pass
def main():
    while True:
        print("\nChoose a task:")
        print("1: Greet the user")
        print("2: Calculate the area of a circle")
        print("3: Calculate rectangle height")
        print("4: Add two numbers")
        print("5: Convert medieval mass units")
        print("6: Generate a random number")
        print("7: Exit")

        choice = input("Enter 1-7: ")

        if choice == "1":
            greet_user()
        elif choice == "2":
            circle_area()
        elif choice == "3":
            rectangle_height()
        elif choice == "4":
            add_values()
        elif choice == "5":
            mass_converter()
        elif choice == "6":
            random_generator()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()