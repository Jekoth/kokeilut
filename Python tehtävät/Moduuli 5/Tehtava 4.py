user_input = []

#Loop asks for 5 input
for i in range(5):
    city = input(f"Enter the names of five cities one by one {i+1}: ")
    user_input.append(city) #Adds input to the list

print("\nThe cities entered are: ")
for city in user_input:
    print(city)