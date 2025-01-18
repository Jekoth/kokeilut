convert = float(input("Enter number in inches: "))

while convert > 0:  #if positive
    cm = convert * 2.54  #Inches to cm formula
    print(f"{convert} inches is {cm} centimeters")
    break

#if not positive
if convert <= 0:
    print("Please enter a positive number.")
