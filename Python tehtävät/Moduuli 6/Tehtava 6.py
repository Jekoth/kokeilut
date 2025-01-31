#func that calculates diameter and price of pizza per square meter
import math

def calculate_diameter_price(diameter, price):
    radius = diameter / 2   #Calculates radius
    area = math.pi * (radius * 2)    #Calculates circle area of the pizza with pi
    square_meters = area / 10000    #Calculates square meters by converting cm2 from area to m2
    unit_price = price / square_meters    # calculates unit price per square meter
    return unit_price

#main

#get first and second pizza input
# compares better value per square meter
