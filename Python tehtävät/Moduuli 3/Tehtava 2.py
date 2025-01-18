cabin_class = input("Choose a cabin class Lux, A, B or C: ")

if(cabin_class == "LUX"):
    print("Lux: upper deck cabin with a balcony")
elif(cabin_class == "A"):
    print("A: above the car deck, equipped with a window")
elif(cabin_class == "B"):
    print("B: windowless cabin above the car deck")
elif(cabin_class == "C"):
    print("C: windowless cabin below the car deck")
else:
    print("invalid cabin class")

