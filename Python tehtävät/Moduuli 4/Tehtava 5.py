username = "python"
password = "rules"
tries = 1

user_name = input("Enter username: ")
user_pass = input("Enter password: ")

while user_name and user_pass != username and password or tries <= 5:
    if user_name == username and user_pass == password:
        print("Welcome")
        break
    else:
        print("Access denied")
        tries = tries + 1

    user_name = input("Enter username: ")
    user_pass = input("Enter password: ")

