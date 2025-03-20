# user input gas and then program converts it to litres until it receives negative value

def fuel_converter(gallons):
    liters = gallons * 3.785 #1 gallon is approx. 3.785 litre
    return liters

while True: #While value is not negative loop continues.
    gallons = int(input("Enter gallons: "))
    if gallons < 0:
        print("Value is negative. Program stopped")
        break
    print(f"{gallons} gallons is {fuel_converter(gallons):.2f} liters.")