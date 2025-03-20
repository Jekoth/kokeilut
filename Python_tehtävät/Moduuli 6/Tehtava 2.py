import random

def dice(sides):
    while True:
        roll = random.randint(1, sides) #Generates random number between 1 and user input
        print("Rolled: ", roll)
        if roll == sides: #checks if rolled number maximum is user input
            break

if __name__ == "__main__":
    sides = int(input("Enter number of sides on the dice: "))
    dice(sides)