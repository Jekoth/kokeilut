number = 1 #factor

#Check if number is divisible by 3 in range of 1, 1000.
while number in range(1, 1000):
    if number % 3 == 0:
        print(number)
    number += 1 # increase every iteration

