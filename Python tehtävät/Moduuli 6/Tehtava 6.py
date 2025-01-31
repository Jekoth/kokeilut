#func that calculates diameter and price of pizza per square meter
import math

def calculate_diameter_price(diameter, price):
    radius = diameter / 2   #Calculates radius
    area = math.pi * (radius * 2)    #Calculates circle area of the pizza with pi
    square_meters = area / 10000    #Calculates square meters by converting cm2 from area to m2
    unit_price = price / square_meters    # calculates unit price per square meter
    return unit_price

def main():
    #get first and second pizza input
    diameter1 = int(input("Enter the diameter of the first pizza in cm: "))
    price1 = int(input("Enter the price of the first pizza in euros: "))

    diameter2 = int(input("Enter the diameter of the first pizza in cm: "))
    price2 = int(input("Enter the price of the first pizza in euros: "))


    # compares better value per square meter
    if price1 < price2:
        print("First pizza is better value")
    elif price1 > price2:
        print("Second pizza is better value")
    else:
        print("Both pizzas have same value")

main()