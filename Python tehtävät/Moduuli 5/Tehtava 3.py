user_input = input("Enter a number: ")

try:
    num = int(user_input)

    if num <= 1: #If input is less or equal to 1 are not prime
        print(f"{num} is not a prime number. ")
    else:
        is_prime = True #Number is prime until it is not divisible by divisors
except ValueError:
    print("Invalid input.")