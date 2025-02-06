#function that return original and even number from the list of integers

def remove_uneven_numbers(input_list):
    even_numbers = [] #even list

    for num in input_list: #checks each number from even list

        if num % 2 == 0:#checks if number is even
            even_numbers.append(num)#if number is even adds it to even list

    return even_numbers#Return list of even numbers

def main():
    original_list = [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 , 10] # original list

    even_list = remove_uneven_numbers(original_list) #removes even numbers from original list

    print("Original list: ", original_list)
    print("Even list: ", even_list)

main()