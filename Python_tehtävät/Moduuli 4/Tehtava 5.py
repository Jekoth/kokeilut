username = "python"
password = "rules"
tries = 1

user_name = input("Enter username: ")
user_pass = input("Enter password: ")

while (user_name != username or user_pass != password) and tries <= 5: #Loop is true until correct credentials are entered
    if user_name == username and user_pass == password:
        print("Welcome!")
        break
    if tries >= 5:
        print("Access denied")
        break
    else:
        print("Incorrect, try again: ")
        tries += 1

    user_name = input("Enter username: ")
    user_pass = input("Enter password: ")

