user_input = input("Enter a number: ")

try:
    num = int(user_input)

    if num <= 1: #If input is less or equal to 1 are not prime
        print(f"{num} is not a prime number. ")
    else:
        is_prime = True #Number is prime until it is not divisible by divisors

        for i in range(2, num):
            if num % i == 0: #If input is divisible it is not a prime number.
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input.")