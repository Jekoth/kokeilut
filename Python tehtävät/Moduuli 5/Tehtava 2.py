num = []

print("Enter Number. Press enter to stop program")

while True:
    user_num = input("Enter a number: ")
    if user_num == "": #Stop program if user enter empty string.
        break
    try:
        number = float(user_num) #Conv string to float
    except ValueError:
        print("Invalid input")