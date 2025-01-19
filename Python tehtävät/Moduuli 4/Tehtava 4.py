import random

num = random.randint(1, 10)

guess_num = int(input("Guess the number between 1-10: "))

while num != guess_num:
    if guess_num < num:
        print("Too low ")
    elif guess_num > num:
        print("Too high ")
    else:
     break
print("Correct! ")