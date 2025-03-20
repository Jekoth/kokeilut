import math
import random
import os

#Tehtävä 1
def greet_user():
    #Asks for user input
    user = input("Enter your name: ")
    print("Hello " + user + "!")
    input("\nPress Enter to continue...")

#Tehtävä 2
def circle_area():
    #Asks user to enter radius
    radius = float(input("Enter a radius: "))
    area = math.pi * radius ** 2
    print("The area is: " + str(area))
    input("\nPress Enter to continue...")

#Tehtävä 3
def rectangle_perimeter():
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))
    #Calculates both sides and multiplies sum to get perimeter of a rectangle
    perimeter = (height + length) * 2
    print(f"Perimeter is: {perimeter}")
    input("\nPress Enter to continue...")

#Tehtävä 4
def add_values():
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    int3 = int(input("Enter third number: "))

    total_sum = int1 + int2 + int3
    times = int1 * int2 * int3
    average = total_sum / 3

    print(f"SUM\n{int1} + {int2} + {int3} = {total_sum}")
    print(f"TIMES\n{int1} x {int2} x {int3} = {times}")
    print(f"AVERAGE\n{total_sum} / 3 = {average}")
    input("\nPress Enter to continue...")

#Tehtävä 5
def mass_converter():
    int1 = int(input("Enter talents: "))
    int2 = int(input("Enter pounds: "))
    int3 = float(input("Enter lots: "))

    talent = 20  # pounds
    pound = 32  # lots
    lot = 13.3  # grams

    #Convert to grams
    total_grams = (
        int1 * talent * pound * lot +
        int2 * pound * lot +
        int3 * lot
    )

    #Convert to kg
    kg = int(total_grams / 1000)
    grams = (total_grams % 1000)

    print(f"The weight in modern units:\n{kg} kilograms and {grams:.2f} grams.")
    input("\nPress Enter to continue...")

#Tehtävä 6
def random_generator():
    digit1 = random.randint(0, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)
    three_digit_code = str(digit1) + str(digit2) + str(digit3) # combine three random digits

    digit4 = random.randint(1, 6)
    digit5 = random.randint(1, 6)
    digit6 = random.randint(1, 6)
    digit7 = random.randint(1, 6)
    four_digit_code = str(digit4) + str(digit5) + str(digit6) + str(digit7) # combine four random digits

    #Print code
    print("3-digit code: ", three_digit_code)
    print("4-digit code: ", four_digit_code)
    input("\nPress Enter to continue...")

def clear_screen():
    # Clears the screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("\nChoose a task number from 1 to 7, or select 7 to exit: ")
        print("1: Greets the user")
        print("2: Calculate the area of a circle")
        print("3: Calculate rectangle perimeter")
        print("4: Sums, times, and average of three integers")
        print("5: Convert medieval mass units")
        print("6: Generate random codes")
        print("7: Exit")

        choice = input("Choose a number from 1 to 7: ")

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