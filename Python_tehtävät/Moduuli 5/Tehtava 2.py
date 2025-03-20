num = []

print("Press enter to stop program")

while True:
    user_num = input("Enter a number: ")
    if user_num == "": #Stop program if user enter empty string.
        break
    try:
        number = int(user_num) #Conv string to int
        num.append(number)
    except ValueError:
        print("Invalid input") #number is added to the empty list

num.sort(reverse=True)

top_num = num[:5] #Splitting reverse sorted list

print("\nThe five top number are: ")
for number in top_num:
    print(number)