import random

random_num = random.randint(1, 10)

guess_num = int(input("Guess the number between 1-10: "))

while random_num != guess_num: #Loop continues as long as guess number is not equal to the random number
    if guess_num < random_num:
        print("Too low ")
    elif guess_num > random_num:
        print("Too high ")

    guess_num = int(input("Try again: "))

print("Correct! ", random_num)