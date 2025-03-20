fish_limit = 42
zander_cm = int(input("What is the length of Zander in Centimeters: "))


if zander_cm >= fish_limit:
    print("Good Catch ")
else:
    below_limit = fish_limit - zander_cm
    print(f"Release Zander fish is {below_limit} below size limit")