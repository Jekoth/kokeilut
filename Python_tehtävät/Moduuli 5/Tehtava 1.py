import random

num_roll = int(input("How many dices to roll? "))
total_sum = 0

for num in range(num_roll):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"The sum of the rolled dice is: {total_sum}")