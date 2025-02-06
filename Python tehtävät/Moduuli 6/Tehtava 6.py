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

    #calculates pizza price and diameter for both pizzas using function
    pizza1_price = calculate_diameter_price(diameter1, price1)
    pizza2_price = calculate_diameter_price(diameter2, price2)


    # compares better value per square meter
    if pizza1_price < pizza2_price:
        print("First pizza is better value")
    elif pizza1_price > pizza2_price:
        print("Second pizza is better value")
    else:
        print("Both pizzas have same value")

main()