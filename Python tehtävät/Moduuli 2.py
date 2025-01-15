import math

#Tehtävä 1
def greet_user():
    #Asks for user input
    user = input("Enter your name: ")
    print("Hello " + user + "!")

#Tehtävä 2
def circle_area():
    #Asks user to enter radius
    radius = float(input("Enter a radius: "))
    area = math.pi * radius ** 2
    print("The area is: " + str(area))

#Tehtävä 3
def rectangle_perimeter():
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))
    #Calculates both sides and multiplies sum to get perimeter of a rectangle
    area = (height + length) * 2
    print(f"{height} + {length} x 2 is: {str(area)}")

#Tehtävä 4
def add_values():
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    int3 = int(input("Enter third number: \n"))

    total_sum = int1 + int2 + int3
    times = int1 * int2 * int3
    average = total_sum / 3

    print(f"SUM\n{int1} + {int2} + {int3} is: {str(total_sum)}")
    print(f"TIMES\n{int1} x {int2} x {int3} is: {str(times)}")
    print(f"AVERAGE\n{total_sum} / 3 is: {str(average)}")

def mass_converter():
    int1 = int(input("Enter talents: "))
    int2 = int(input("Enter pounds: "))
    int3 = float(input("Enter lots: \n"))

    talent = 20 #pounds
    pound = 32 #lots
    lot = 13.3 #grams

    #conver to grams
    gram = (
        int1 * talent * pound * lot +
        int2 * pound * lot +
        int3 * lot
    )
    print(f"The weight in modern units:\n kilograms and grams.")

def random_generator():
    pass
def main():
    while True:
        print("\nChoose a task number from 1 to 6, or select 7 to exit: ")
        print("1: Greets the user")
        print("2: Calculate the area of a circle")
        print("3: Calculate rectangle perimeter")
        print("4: Sums, times and average of three integer")
        print("5: Convert medieval mass units")
        print("6: Generate a random number\n")
        print("7: Exit")

        choice = input("Choose a number from 1 to 6: ")

        if choice == "1":
            greet_user()
        elif choice == "2":
            circle_area()
        elif choice == "3":
            rectangle_perimeter()
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