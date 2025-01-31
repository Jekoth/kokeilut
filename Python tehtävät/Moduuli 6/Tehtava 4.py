# sums numbers from list and prints returned value from main

def sum_list (numbers):
    return sum(numbers)

def main():
    number_list = [1, 2,3,4,5]
    result = sum_list(number_list) #result is sum of numbers from the list
    print("The sum of numbers is: ", result)

main() #calls main function