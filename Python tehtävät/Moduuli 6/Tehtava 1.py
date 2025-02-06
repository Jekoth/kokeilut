import random

def roll_dice():
    return random.randint(1, 6)

def dice():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print("Rolled: ", roll)

if __name__ == "__main__":
    dice()