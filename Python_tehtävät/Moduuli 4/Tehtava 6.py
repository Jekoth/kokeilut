import random

num_points = int(input("Enter the number of random points to generate: "))

if num_points <= 0:
    print("Please enter a positive number: ")
else:
    points_inside_circle = 0
    total_points = 0

    #Loop that generates random points
    while total_points < num_points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        #This checks if points are inside the circle
        if x**2 + y**2 < 1:
            points_inside_circle += 1

        total_points += 1

    #Calculates approx of pi and displays it
    pi_approx = 4 * points_inside_circle / num_points
    print("Approximation of pi: ", pi_approx)
